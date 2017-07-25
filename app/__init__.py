# app/__init__.py
"""Module initialization
"""

# third-party imports
from flask import Flask

# local imports
from config import APP_CONFIG

APP = Flask(__name__, instance_relative_config=True)

from app import views

APP.config.from_object(APP_CONFIG['development'])
