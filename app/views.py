# views.py
"""Main Program -
Data is stored in class variables
for module application
"""
from flask import render_template, redirect, session
from flask import request

from app import APP
from app.application import Application

USER = Application()

@APP.route('/')
def index():
    """Index page render
    """
    return render_template('index.html')

@APP.route('/signup')
def sign_up():
    """Register user
    """
    return render_template('index.html')

@APP.route('/login')
def log_in():
    """Login user
    """
    return render_template('index.html')
