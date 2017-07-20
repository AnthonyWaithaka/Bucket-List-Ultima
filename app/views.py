# app/views.py

from flask import render_template
from flask import Blueprint
from flask_login import login_required
from . import app
homer = Blueprint('homer', __name__)
app.register_blueprint(homer)

@homer.route('/')
def homepage():
    """Render homepage template on / route
    """
    return render_template('/home/index.html', title="Welcome")

@homer.route('/dashboard')
@login_required
def dashboard():
    """Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")