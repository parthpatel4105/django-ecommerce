# 🛒 Django + React E-Commerce Web App

This is a full-stack e-commerce application built with **Django** for the backend and **React.js** for the frontend.

---

## 📁 Project Structure

/backend/ --> Django REST API
/frontend/ --> React eCommerce UI


---

## 🚀 Features

- 🧾 Product listing and detail pages
- 🛒 Add to cart / remove from cart
- 📦 Order placement
- 🧑 Admin panel (Django)
- 🌐 API using Django REST Framework

---

## 🔧 Tech Stack

- **Frontend**: React, Axios, Bootstrap/Tailwind
- **Backend**: Django, Django REST Framework
- **Database**: SQLite 
- **Auth**: Token-based 

---

### 1️⃣ Backend (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

cd frontend
npm install
npm start


Backend .env (example)

SECRET_KEY=your_secret_key_here
DEBUG=True

Frontend .env (example)

REACT_APP_API_URL=http://127.0.0.1:8000/api/
