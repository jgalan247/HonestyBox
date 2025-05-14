import os
from flask import Flask
from .extensions import db, jwt
from .routes.auth import auth_bp
from .routes.farmer import farmer_bp
from .routes.admin import admin_bp
from .html_routes import html_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret-key'
    
    # Always use DB path relative to this file
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, '..', 'honestybox.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'another-secret-key'

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(farmer_bp, url_prefix='/api/farmer')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(html_bp)

    print("🧠 Using DB:", app.config['SQLALCHEMY_DATABASE_URI'])  # Optional

    return app

