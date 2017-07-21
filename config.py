# config.py
"""Testing configurations
for different app uses
"""

class Config(object):
    """Common configurations
    """

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