from datetime import datetime
from sms_app import db


class SMS(db.Model):
    __tablename__ = 'SMS'
    person_id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    cell_phone = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')
    date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    response_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    optout_ind = db.Column(db.String(10), nullable=False, default='N')

    def __repr__(self):
        return f"Patient('{self.person_id}', '{self.cell_phone}', '{self.status}', '{self.date_sent}','{self.response_date}', '{self.optout_ind}')"
