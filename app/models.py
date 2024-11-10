# app/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def timestamp_jst(self):
        return self.timestamp.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Tokyo'))