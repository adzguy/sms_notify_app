from sqlalchemy import func
from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, Blueprint, abort, Response
from functools import wraps
from twilio.request_validator import RequestValidator

from sms_app.main.forms import SendMessageForm
from sms_app import db
from sms_app.models import SMS
from sms_app.config import Config
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

account_sid = Config.TWILIO_ACCOUNT_SID
auth_token = Config.TWILIO_AUTH_TOKEN
twilio_messaging_sid = Config.TWILIO_MESSAGING_SID
client = Client(account_sid, auth_token)


main = Blueprint('main', __name__)


def validate_twilio_request(f):
    """Validates that incoming requests genuinely originated from Twilio"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Create an instance of the RequestValidator class
        validator = RequestValidator(auth_token)

        # Validate the request using its URL, POST data,
        # and X-TWILIO-SIGNATURE header
        request_valid = validator.validate(
            request.url,
            request.form,
            request.headers.get('X-TWILIO-SIGNATURE', ''))

        # Continue processing the request if it's valid, return a 403 error if
        # it's not
        if request_valid:
            return f(*args, **kwargs)
        else:
            return abort(403)
    return decorated_function


@main.route('/', methods=["GET", "POST"])
@main.route('/notifications', methods=["GET", "POST"])
def notifications() -> Response:
    form = SendMessageForm()
    if form.validate_on_submit():
        # patients = SMS.query.filter(SMS.optout_ind == 'N').group_by(
        #     SMG_SMS_Log.cell_phone).having(func.count(SMS.cell_phone) > 1).all()

        patients = SMS.query.filter(
            SMS.optout_ind == 'N', SMS.service == 'COVID Schedule numbers #3').all()

        # patients = SMS.query.with_entities(SMG_SMS_Log.cell_phone).distinct().filter(
        #     SMS.optout_ind == 'N', SMS.service == 'COVID Schedule numbers #3').all()

        if len(patients) > 0:
            flash('Messages on their way!')
            for patient in patients:
                try:
                    message = client.messages.create(
                        body=form.message.data,
                        messaging_service_sid=twilio_messaging_sid,
                        to=patient.cell_phone
                    )
                    patient.date_sent = datetime.utcnow()
                    patient.status = message.status
                    db.session.commit()
                except Exception as e:
                    patient.service = 'COVID SMS cell_phone format error'
                    print(e)
                    continue
        else:
            flash('No opted in patients found for notifications in the database!')
        form.reset()
        return redirect(url_for('main.notifications'))
    return render_template('notifications.html', title='SMS Notify', form=form)


# webhook to Twilio
@main.route('/message', methods=["POST"])
@validate_twilio_request
def message() -> Response:

    patients = SMS.query.filter(
        SMS.cell_phone == request.form['From'][2:]).all()

    body = request.form['Body']
    opt_out_words = ('stop', 'cancel', 'end', 'quit', 'stopall', 'unsubscribe')
    opt_in_words = ('start', 'unstop', 'yes')

    if len(patients) > 0:
        for patient in patients:
            if body.lower().strip() in opt_out_words and patient.optout_ind == 'N':
                patient.optout_ind = 'Y'
            elif body.lower().strip() in opt_in_words and patient.optout_ind == 'Y':
                patient.optout_ind = 'N'

            patient.response_date = datetime.utcnow()
            db.session.commit()

    resp = MessagingResponse()
    return str(resp)
