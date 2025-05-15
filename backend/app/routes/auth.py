from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import User
from passlib.hash import argon2
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email    = data.get('email')
    lat      = data.get('lat')
    lon      = data.get('lon')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    password_h = argon2.hash(password)

    new_user = User(
        username=username,
        password_h=password_h,
        email=email,
        lat=lat,
        lon=lon,
        role="pending",          # default until approved by admin
        confirmed=False
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered, pending approval"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"🔐 Login attempt for: {username} with password: {password}")

    user = User.query.filter_by(username=username).first()
    if not user:
    	print("🧩 Login failed: user not found")
    	return jsonify({"msg": "Invalid username or password"}), 401

    print("🔐 Stored hash:", user.password_h)

    try:
    	if not argon2.verify(password, user.password_h):
        	print("🧩 Login failed: password mismatch")
        	return jsonify({"msg": "Invalid username or password"}), 401
    except Exception as e:
    	print("💥 Error during password verification:", e)
    	return jsonify({"msg": "Password verification error"}), 500

    if not user.confirmed:
    	print("⏳ Login blocked: user not confirmed")
    	return jsonify({"msg": "Account not yet confirmed"}), 403

    print("✅ Login success for:", username)

    if not user.confirmed:
        return jsonify({"msg": "Account not yet confirmed"}), 403

    access_token = create_access_token(identity=str(user.id))
    return jsonify(access_token=access_token), 200

