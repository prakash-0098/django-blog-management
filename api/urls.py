from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('posts/', views.create_post_list, name='create_post_list'),
    path('posts/<int:pk>', views.modify_post, name='modify_post'),
    path('posts/<int:pk>/comments/', views.create_comments_list, name='create_comments_list'),
    path('posts/<int:pk>/likes/', views.add_likes, name='add_likes'),
    path('posts/<int:pk>/unlikes/', views.delete_likes, name='delete_likes')
]