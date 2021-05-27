from sms_app.main.forms import SendMessageForm
from tests.base import BaseTestCase


class FormTests(BaseTestCase):
    # Ensures populate SenMessageForm with missing message filed give an error
    def test_populate_SendMessageForm_with_missing_message_should_produce_error(self):
        # arrange
        form = SendMessageForm(message='')

        # assert
        assert form.validate() is False
        assert 'Message is required' in form.message.errors
