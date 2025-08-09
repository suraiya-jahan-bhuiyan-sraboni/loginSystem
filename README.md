# Flask + MongoDB Login & Registration API

A simple REST API for user login and registration using Flask and MongoDB.

---

## Features

- User registration with email and password  
- User login with email and password  
- Passwords securely hashed with bcrypt  
- MongoDB as the database backend (Atlas or local)  
- Simple and clean API design

---

## Prerequisites

- Python 3.10 or higher  
- MongoDB Atlas account or local MongoDB server  
- Git (optional, for cloning repository)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/suraiya-jahan-bhuiyan-sraboni/loginSystem.git)
cd loginSystems
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key_here
```

* Use your MongoDB Atlas connection string or local MongoDB URI for `MONGO_URI`.
* `SECRET_KEY` can be any random string (used for Flask session security if needed).

### 4. Run the application

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

---

## API Endpoints

### Register

* **URL:** `/register`
* **Method:** `POST`
* **Request Body:**

```json
{
  "email": "user@example.com",
  "password": "your_password"
}
```

* **Response:**

```json
{
  "message": "User registered successfully"
}
```

---

### Login

* **URL:** `/login`
* **Method:** `POST`
* **Request Body:**

```json
{
  "email": "user@example.com",
  "password": "your_password"
}
```

* **Response (success):**

```json
{
  "message": "Login successful"
}
```

* **Response (failure):**

```json
{
  "message": "Invalid credentials"
}
```
