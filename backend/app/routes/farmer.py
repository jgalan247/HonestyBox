from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Product

farmer_bp = Blueprint('farmer_bp', __name__)

@farmer_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def farmer_dashboard():
    user = get_jwt_identity()
    if user['role'] != 'farmer':
        return jsonify({"msg": "Unauthorized"}), 403
    return jsonify({"msg": f"Welcome, farmer {user['id']}!"})

@farmer_bp.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    user = get_jwt_identity()
    products = Product.query.filter_by(owner_id=user['id']).all()
    return jsonify([p.to_dict() for p in products]), 200

@farmer_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    user = get_jwt_identity()
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        available=data.get('available', 'yes'),
        location_id=data.get('location_id'),
        owner_id=user['id']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@farmer_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    user = get_jwt_identity()
    product = Product.query.filter_by(id=product_id, owner_id=user['id']).first()
    if not product:
        return jsonify({"msg": "Product not found"}), 404

    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.available = data.get('available', product.available)
    db.session.commit()
    return jsonify(product.to_dict()), 200

@farmer_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    user = get_jwt_identity()
    product = Product.query.filter_by(id=product_id, owner_id=user['id']).first()
    if not product:
        return jsonify({"msg": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"msg": "Product deleted"}), 200

