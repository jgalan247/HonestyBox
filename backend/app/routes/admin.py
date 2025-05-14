from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/users/pending', methods=['GET'])
@jwt_required()
def get_pending_users():
    user = get_jwt_identity()
    if user['role'] != 'admin':
        return jsonify({"msg": "Admin access only"}), 403

    # This will be replaced with actual DB query later
    return jsonify({"pending_users": []})

def confirm_user(user_id):
    admin = get_jwt_identity()
    if admin['role'] != 'admin':
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
