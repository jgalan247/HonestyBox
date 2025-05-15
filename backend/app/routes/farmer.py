from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import User, Product

farmer_bp = Blueprint('farmer_bp', __name__)

@farmer_bp.route('/products', methods=['GET'])
@jwt_required()
def get_my_products():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    if user.role != 'farmer':
        return jsonify({"msg": "Forbidden"}), 403

    products = Product.query.filter_by(owner_id=user.id).all()
    return jsonify([p.to_dict() for p in products])  # ✅ Use the model's to_dict()
    

@farmer_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    if user.role != 'farmer':
        return jsonify({"msg": "Forbidden"}), 403

    data = request.get_json()
    product = Product(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price'),
        available=data.get('available'),
        owner_id=user.id
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"msg": "Product created", "id": product.id}), 201


@farmer_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    product = Product.query.get(product_id)
    if not product or product.owner_id != user.id:
        return jsonify({"msg": "Not found or unauthorized"}), 404

    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.available = data.get('available', product.available)

    db.session.commit()
    return jsonify({"msg": "Product updated"}), 200


@farmer_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    product = Product.query.get(product_id)
    if not product or product.owner_id != user.id:
        return jsonify({"msg": "Not found or unauthorized"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"msg": "Product deleted"}), 200

