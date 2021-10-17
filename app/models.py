from app import db, login_manager
from datetime import datetime as dt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

