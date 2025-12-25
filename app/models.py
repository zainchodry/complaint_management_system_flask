from app.extenshions import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)

    status = db.Column(db.String(50), default='Submitted')
    admin_review = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    complaint_id = db.Column(db.Integer, db.ForeignKey('complaint.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
