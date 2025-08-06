# book
📚 Book Catalog API

A Django REST API to manage a book catalog with Docker, CI/CD, and Kubernetes support.

---

 🚀 Project Overview

This project provides a RESTful API for managing a collection of books. It supports full CRUD operations and includes containerization with Docker, CI/CD with GitHub Actions, and deployment via Kubernetes using Helm.

---

 🔧 Local Development

1. Clone and Setup
```bash
git clone https://github.com/your-username/book-catalog.git
cd book-catalog
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Run the Server
python manage.py migrate
python manage.py runserver
🧪 API Usage Examples
List Books: GET /api/books/
Create Book: POST /api/books/
Retrieve Book: GET /api/books/{id}/
Update Book: PUT /api/books/{id}/
Delete Book: DELETE /api/books/{id}/
JSON example:
{
  "title": "Django Unleashed",
  "author": "Will Vincent",
  "isbn": "9781234567897",
  "published_date": "2020-01-01",
  "description": "A powerful Django book"
}
🔄 CI/CD Pipeline (GitHub Actions)
Lint & test: Automatically run tests on push.
Build Docker image: Using Dockerfile
Push to GitHub Container Registry: With GitHub Actions secrets
Deploy via Helm: After successful build
☸️ Kubernetes + Helm
Install with Helm:
helm install bookcatalog ./books-catalog-chart
Ensure your kubectl is configured to the correct context (e.g., local k3d or Minikube).
📦 Docker Commands
Build & run locally:
docker build -t bookcatalog:latest .
docker run -p 8000:8000 bookcatalog
✅ API Implementation
Full CRUD for books
Model fields:
title
author
isbn
published_date
description
Validated with Django REST Framework serializers
Includes unit tests using Django TestCase
