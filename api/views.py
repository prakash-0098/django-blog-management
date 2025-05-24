from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from core.models import Post, Comments, Likes

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAuthenticated])
def create_post_list(request):
    if request.method == 'GET':
        try:
            post = Post.objects.filter(author=request.user)
            serializer = PostSerializer(post, many=True)
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        except Post.DoesNotExist:
            return Response({
                'message': 'Post not found'
            }, status = status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['GET','PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def modify_post(request, pk):
    try:
        post = Post.objects.get(pk=pk, author=request.user)
    except Post.DoesNotExist:
        return Response({
            'message': 'Post not found' 
        }, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST', 'GET'])
@authentication_classes([])           # disable JWT
@permission_classes([AllowAny])       # allow everyone
def create_comments_list(request, pk):
    if request.method == 'GET':
        try:
            comments = Comments.objects.filter(post=pk)
            serializer = CommentSerializer(comments, many=True)
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        except:
            return Response({
                'message': 'Comments not found'
            }, status = status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
@authentication_classes([]) # disable JWT
@permission_classes([AllowAny]) # allow everyone
def add_likes(request, pk):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['DELETE'])
@authentication_classes([]) # disable JWT
@permission_classes([AllowAny])
def delete_likes(request, pk):
    try:
        like = Likes.objects.get(post=pk)
    except Likes.DoesNotExist:
        return Response({
            'message': 'Not found'
        })

    like.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)