# 🎬 Movie Management Platform

A web platform that allows users to upload, manage, and stream movies using a Django REST API backend. Video uploads are processed asynchronously (e.g., generating thumbnails) using Celery and Redis. The backend is fully containerized with Docker and secured using JWT authentication.

---

## 🧱 Tech Stack

**Backend:**
- Python 3.10
- Django
- Django REST Framework (DRF)
- Celery 5.x
- Redis (as message broker)
- Pillow (for image processing)
- JWT (via `djangorestframework-simplejwt`)

**Containerization:**
- Docker + Docker Compose

- Used with `venv`. Just run for linux/mac
```bash
source venv/bin/activate
```

---

## 🔧 Prerequisites

| Tool           | Version          |
|----------------|------------------|
| Python         | 3.10+            |
| Node.js        | 18+ (for frontend)|
| Docker         | 20.x+            |
| Docker Compose | v2+              |
| Postman        | (for API testing) |

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/movie-management-platform.git
cd movie-management-platform
docker compose build
docker compose up