from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class SendMessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[
        DataRequired(message="Message is required")])
    submit = SubmitField('Send SMS')

    def reset(self):
        blankData = MultiDict([('message', '')])
        self.process(blankData)
