from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password_h = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    lat = db.Column(db.Text)
    lon = db.Column(db.Text)
    role = db.Column(db.Text, default="pending")  # e.g. "farmer", "admin"
    confirmed = db.Column(db.Boolean, default=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Text)
    available = db.Column(db.Text)  # "yes" or "no"
    location_id = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "available": self.available,
            "location_id": self.location_id
        }

