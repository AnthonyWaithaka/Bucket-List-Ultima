# app/__init__.py
"""Flask Initialization -
used by the run.py file
"""

# third-party imports
from flask import Flask
from flask_login import LoginManager

# local imports
from config import APP_CONFIG

login_manager = LoginManager()

def create_app(config_name):
    """Initializing Flask
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    return app
