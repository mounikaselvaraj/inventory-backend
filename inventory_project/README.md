# 📦 Inventory Management API

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-REST-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-red)
![Swagger](https://img.shields.io/badge/API-Swagger-brightgreen)

A **Django REST Framework backend project** for inventory management with authentication, search/filter, and API documentation.

---

## 🚀 Features
- JWT Authentication (Login system)
- CRUD operations for items
- Search & filter (low stock)
- MySQL database integration
- Swagger API documentation

---

## 📌 API Endpoints

### Auth
- POST `/api/token/`
- POST `/api/token/refresh/`

### Items
- GET `/items/`
- POST `/items/`
- GET `/items/<id>/`
- PUT `/items/<id>/`
- DELETE `/items/<id>/`

---

## 🔍 Filters
- `/items/?search=name`
- `/items/?low_stock=true`

---

## 📘 API Docs
- Swagger → `/swagger/`
- Redoc → `/redoc/`

---

## ⚙️ Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver