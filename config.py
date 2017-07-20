# config.py
"""File used by Flask to
determine run settings
"""

class Config(object):
    """Common configurations
    """
    # Configurations common across all environments

class DevelopmentConfig(Config):
    """Development configurations
    """
    DEBUG = True

class ProductionConfig(Config):
    """Production configurations
    """
    DEBUG = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
