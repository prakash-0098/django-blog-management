
# 📝 Blog API with Comments and Likes

A Django REST Framework project that allows users to create blog posts, comment on them, and like/unlike posts.

---

## ✅ Features

- User Registration & Authentication (Token-based)
- Create, Read, Update, Delete (CRUD) for Blog Posts
- Comment on Posts
- Like and Unlike Posts
- Filter Posts by Author
- View number of comments and likes

---

## 📦 Requirements

```bash
Django>=4.0
djangorestframework
djangorestframework-simplejwt
```

Install with:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Project Structure

```
blog_api/
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── blog_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```

---

## 🧱 Models Overview

### 🔹 User (built-in)

### 🔹 Post
```python
title: CharField
content: TextField
author: ForeignKey(User)
created_at: DateTimeField
updated_at: DateTimeField
```

### 🔹 Comment
```python
post: ForeignKey(Post)
author: ForeignKey(User)
content: TextField
created_at: DateTimeField
```

### 🔹 Like
```python
post: ForeignKey(Post)
user: ForeignKey(User)
created_at: DateTimeField
```

---

## 🌐 API Endpoints

### 🔐 Authentication

| Method | Endpoint          | Description            |
|--------|-------------------|------------------------|
| POST   | `/api/register/`  | Register new user      |
| POST   | `/api/token/`     | Get JWT token          |
| POST   | `/api/token/refresh/` | Refresh JWT token |

---

### 📄 Blog Posts

| Method | Endpoint               | Description            |
|--------|------------------------|------------------------|
| GET    | `/api/posts/`          | List all posts         |
| POST   | `/api/posts/`          | Create new post        |
| GET    | `/api/posts/<id>/`     | View post details      |
| PUT    | `/api/posts/<id>/`     | Update post            |
| DELETE | `/api/posts/<id>/`     | Delete post            |

---

### 💬 Comments

| Method | Endpoint                           | Description            |
|--------|------------------------------------|------------------------|
| GET    | `/api/posts/<id>/comments/`        | List comments for post |
| POST   | `/api/posts/<id>/comments/`        | Add comment to post    |

---

### ❤️ Likes

| Method | Endpoint                     | Description         |
|--------|------------------------------|---------------------|
| POST   | `/api/posts/<id>/like/`      | Like a post         |
| DELETE | `/api/posts/<id>/unlike/`    | Unlike a post       |

---

## 🏁 Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/yourname/blog_api.git
   cd blog_api
   ```

2. Create virtual environment and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run development server:
   ```bash
   python manage.py runserver
   ```

6. Access API at: `http://localhost:8000/api/`

---

## 📌 Optional Enhancements

- Pagination
- Tagging support
- Search by post title/content
- Swagger or ReDoc API documentation

---

## 🧑‍💻 Author

Made with ❤️ using Django REST Framework.
