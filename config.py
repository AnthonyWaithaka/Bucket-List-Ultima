# config.py
"""Testing configurations
for different app uses
"""

class Config(object):
    """Common configurations
    """
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'default-secret-key'

class DevelopmentConfig(Config):
    """Development configurations
    """
    DEBUG = True

class ProductionConfig(Config):
    """Production configurations
    """
    DEBUG = False

class TestingConfig(Config):
    """Testing configurations
    """
    TESTING = True

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}