from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from config import Config 
app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

app.app_context().push()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Increased length to accommodate hashed password
    role = db.Column(db.String(20), nullable=False)
    
    def __init__(self, username, password, role):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.role = role

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class influencer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    platform = db.Column(db.String(60),nullable=False)
    insta = db.Column(db.String(50))
    facebook = db.Column(db.String(50))
    youtube = db.Column(db.String(50))
    snapchat = db.Column(db.String(50))
    niche = db.Column(db.String(50))
    followers = db.Column(db.Integer)
    bio = db.Column(db.String(100), nullable=False)
    