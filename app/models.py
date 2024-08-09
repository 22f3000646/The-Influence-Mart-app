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
    username = db.Column(db.String(50), unique=True,primary_key=True)
    password = db.Column(db.String(60), nullable=False)  
    role = db.Column(db.String(20), nullable=False)
    
    influencer = db.relationship('Influencer',back_populates='User',cascade='all, delete-orphan')
    
    def __init__(self, username, password, role):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.role = role

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Influencer(db.Model):
    influencer_id =  db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50),db.ForeignKey('user.username'))
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    niche = db.Column(db.String(50))
    role=db.Column(db.String(20) ,default = 'Influencer')
    
    user = db.relationship('User',back_populates='Influencer')
    profile = db.relationship('Profile',back_populates='Influencer',cascade='all, delete-orphan')
    
    def __init__(self,full_name,username,password,email,phone,bio,niche):
        self.full_name = full_name
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.email =  email
        self.phone = phone
        self.bio = bio
        self.niche = niche
    
    
class Profiles(db.Model):
    influencer_id =  db.Column(db.Integer,db.ForeignKey('influencer.id'),primary_key=True)
    insta = db.Column(db.String(50))
    facebook = db.Column(db.String(50))
    youtube = db.Column(db.String(50))
    snapchat = db.Column(db.String(50))
    reach = db.Column(db.Integer)
    
    influencer = db.relationship('Influencer',back_populates='Profiles')
    
    def __init__(self,insta,facebook,youtube,snapchat):
        self.insta = insta
        self.facebook = facebook
        self.youtube = youtube
        self.snapchat = snapchat
    
    def reach(self):
        self.reach = 0.40*(self.youtube)+0.30*(self.insta)+0.20*(self.facebook)+0.10*(self.snapchat)

class Sponsor(db.Model):
    sponsor_id = db.Column(db.Integer)
    first_name = db.Column(db.String(50))
    last_name =  db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20)) 
    password = db.Column(db.String(50))

class Campaign(db.Model):
    campaign_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    campaign_title = db.Column(db.String(20))
    category = db.Column(db.String(20))
    about = db.Column(db.String(100))
    total_request = db.Coloumn(db.Integer)
    status = db.Column(db.String(10))
    
class ad_request(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    campaign_id = db.Column(db.Integer)
    Influencer_id = db.Column(db.Integer)
    infl_username = db.Column(db.String(50))
    response = db.Column(db.String(20))
    followers = db.Column(db.Integer)
    
    
    
    
    