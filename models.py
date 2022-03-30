import sqlite3
from flask_sqlalchemy import SQLAlchemy
from app.py import *
db=SQLAlchemy()

class User(UserMixin, db.Model):
    """User model"""
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    