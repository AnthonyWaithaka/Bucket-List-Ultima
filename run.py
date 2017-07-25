# run.py
"""Application run file
"""
from app import APP

APP.secret_key = "secret key"
APP.debug = True

if __name__ == '__main__':
    APP.run()
