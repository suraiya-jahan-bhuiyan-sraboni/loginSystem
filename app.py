from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
import datetime
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
CORS(app)

users_collection = mongo.db.users

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    users_collection.insert_one({
        "email": email,
        "password": hashed_password
    })

    return jsonify({"message": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({"email": email})
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Login successful"}), 200


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)