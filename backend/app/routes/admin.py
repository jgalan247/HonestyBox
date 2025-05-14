from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import User

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/users/pending', methods=['GET'])
@jwt_required()

def get_pending_users():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if user.role != 'admin':
        return jsonify({"msg": "Admin access required"}), 403

    pending_users = User.query.filter_by(confirmed=False).all()
    return jsonify([
        {"id": u.id, "username": u.username, "email": u.email, "role": u.role}
        for u in pending_users
    ]), 200
def confirm_user(user_id):
    admin_id = get_jwt_identity()
    admin = User.query.get(int(admin_id))
    if admin.role != 'admin':
        return jsonify({"msg": "Admin access required"}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    if user.confirmed:
        return jsonify({"msg": "User already confirmed"}), 400

    user.confirmed = True
    user.role = "farmer"
    db.session.commit()
    return jsonify({"msg": f"User '{user.username}' confirmed as farmer."}), 200

@admin_bp.route('/users/pending', methods=['GET'])
@jwt_required()
def list_pending_users():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if user.role != 'admin':
        return jsonify({"msg": "Admin access required"}), 403

    pending_users = User.query.filter_by(confirmed=False).all()
    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role
        }
        for u in pending_users
    ]), 200

@admin_bp.route('/confirm/<int:user_id>', methods=['POST'])
@jwt_required()
def confirm_user(user_id):
    admin_id = get_jwt_identity()
    admin = User.query.get(int(admin_id))
    if admin.role != 'admin':
        return jsonify({"msg": "Admin access required"}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    if user.confirmed:
        return jsonify({"msg": "User already confirmed"}), 400

    user.confirmed = True
    user.role = "farmer"
    db.session.commit()
    return jsonify({"msg": f"User '{user.username}' has been confirmed as a farmer."}), 200

