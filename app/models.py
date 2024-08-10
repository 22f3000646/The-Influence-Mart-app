from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from config import Config 
app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

app.app_context().push()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True,primary_key=True)
    password = db.Column(db.String(60), nullable=False) 
    
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')) 

class Influencer(db.Model):
    influencer_id =  db.Column(db.Integer,primary_key = True)
    full_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50),primary_key=True)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    niche = db.Column(db.String(50))
    role =db.Column(db.String(20) ,default ='Influencer')
    flagged = db.Column(db.String(20) ,default='False')

    def __init__(self,password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        
    platform = db.relationship('Social_media',backref = 'influencer')
    ad_request = db.relationship('Ad_request',backref = 'influencer',secondary ='Association')
       
class Social_media(db.Model):
    influencer_id =  db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'),primary_key=True)
    Platform = db.Column(db.String(50), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)
     
class Sponsor(db.Model):
    sponsor_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50))
    last_name =  db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True,primary_key=True)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20)) 
    password = db.Column(db.String(50))
    role = db.Column(db.String(20) ,default='sponsor')
    flagged = db.Column(db.String(20) ,default='False')
    
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')) 

class Campaign(db.Model):
    sponsor_id = db.Column(db.Integer,db.ForeignKey('sponsor.sponsor_id'))
    campaign_id = db.Column(db.Integer,primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    campaign_title = db.Column(db.String(20))
    category = db.Column(db.String(20))
    about = db.Column(db.String(100))
    total_request = db.Column(db.Integer)
    status = db.Column(db.String(10))
    payment = db.Column(db.String(10) )
    payment_id = db.Column(db.Integer)
    approvement = db.Column(db.String(10),default='False')
    
    request = db.relationship('Ad_request',backref='campaign')
        
class Ad_request(db.Model):
    ad_request_id = db.Column(db.Integer,primary_key=True)
    campaign_id = db.Column(db.Integer,db.ForeignKey('campaign.campaign_id'))
    Influencer_id = db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'))
    infl_username = db.Column(db.String(50),db.ForeignKey('influencer.username'))
    response = db.Column(db.String(20),default='False')
    followers = db.Column(db.Integer)
    remarks = db.Column(db.String(20))
    
class  Association(db.Model):
    Influencer_id = db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'))
    ad_request_id = db.Column(db.Integer,db.ForeignKey('ad_request.ad_request_id'),primary_key=True)
    