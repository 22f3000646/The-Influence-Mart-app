from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
app=Flask(__name__)
db=SQLAlchemy()
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    password = db.Column(db.String(50),nullable=False)
    role = db.Column(db.String(20),nullable=False)
    
    def __init__(self,username,password,role):
        self.username=username
        self.password=bcrypt.hashpw(password)