from flask import Blueprint, render_template

html_bp = Blueprint('html_bp', __name__)

@html_bp.route('/')
def index():
    return "<h2>Welcome to HonestyBox Backend</h2><p>Visit /admin for the admin dashboard.</p>"

@html_bp.route('/admin')
def admin_page():
    return render_template("admin_page.html")

