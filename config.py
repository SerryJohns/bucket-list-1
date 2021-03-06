import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists('config.env'):
    print('Importing environment from .env file')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]


class Config(object):
    if os.environ.get('APP_NAME'):
        APP_NAME = os.environ.get('APP_NAME')
    else:
        APP_NAME = 'bucket-list'
    if os.environ.get('SITE_URL'):
        SITE_URL = os.environ.get('SITE_URL')
    else:
        SITE_URL = "http://127.0.0.1:5000/api/v1/"
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SO{\xfd~X\xdeZg1`\xe6\xa6\xee\xa7\x8e\xa1Y&\xbdo#\xde\xb7'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'prod_db.sqlite')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev_db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test_db.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
