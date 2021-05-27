import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_MESSAGING_SID = os.environ.get('TWILIO_MESSAGING_SID')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tests.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
