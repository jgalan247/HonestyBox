# backend/seed.py
from app import app, db
from models import Farmer, Product


with app.app_context():

	db.drop_all()
	db.create_all()

	farmers = [
    Farmer(id=1, name="Alice Farm", email="alice@farm.com", role="farmer", confirmed=True, lat=49.225, lon=-2.05),
    Farmer(id=2, name="Bob’s Veggies", email="bob@farm.com", role="farmer", confirmed=False, lat=49.215, lon=-2.08),
    Farmer(id=3, name="Sunny Produce", email="sunny@farm.com", role="farmer", confirmed=True, lat=49.235, lon=-2.09),
    Farmer(id=4, name="Super Sam", email="admin@honestybox.je", role="superadmin", confirmed=True)
	]

	products = [
    Product(name="Free Range Eggs", price=2.5, description="A dozen farm eggs", available="yes", farmer_id=1),
    Product(name="Cherry Tomatoes", price=1.8, description="250g punnet, very sweet", available="yes", farmer_id=1),
    Product(name="Jersey Potatoes", price=3.0, description="Freshly dug 2kg", available="yes", farmer_id=3),
    Product(name="Honey Jar", price=4.0, description="Local wildflower honey", available="no", farmer_id=3),
]

db.session.add_all(farmers + products)
db.session.commit()
print("Database seeded successfully.")


