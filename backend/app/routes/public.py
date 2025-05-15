from flask import Blueprint, jsonify
from app.models import User, Product

public_bp = Blueprint("public_bp", __name__)

@public_bp.route("/api/public/farms", methods=["GET"])
def get_public_farms():
    # Get confirmed farmers
    farmers = User.query.filter_by(role="farmer", confirmed=True).all()
    
    data = []
    for farmer in farmers:
        products = Product.query.filter_by(owner_id=farmer.id).all()
        data.append({
            "farmer_id": farmer.id,
            "farmer_name": farmer.username,
            "lat": farmer.lat,
            "lon": farmer.lon,
            "products": [
                {
                    "name": p.name,
                    "description": p.description,
                    "price": p.price,
                    "available": p.available
                }
                for p in products
            ]
        })

    return jsonify(data)

