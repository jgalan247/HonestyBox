from app import create_app
from app.extensions import db
from app.models import User

app = create_app()
with app.app_context():
    admin = User.query.filter_by(username="admin").first()
    if admin:
        print("✅ Found admin user in DB:")
        print("Username:", admin.username)
        print("Hashed Password:", admin.password_h)
        print("Confirmed:", admin.confirmed)
        print("Role:", admin.role)
    else:
        print("❌ No admin user found.")

