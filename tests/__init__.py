from sms_app.config import TestConfig
from sms_app import create_app, db

twilio_settings = {
    'app': None,
    'db': None,
}


def init_test_environment():
    twilio_settings['app'] = create_app(TestConfig)
    twilio_settings['db'] = db


def test_app():
    return twilio_settings['app']


def test_db():
    return twilio_settings['db']
