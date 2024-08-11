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
    
    def __init__(self, id,username, password):
        self.id = id 
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8')) 

class Influencer(db.Model):
    influencer_id =  db.Column(db.Integer,primary_key = True,autoincrement =True)
    full_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    niche = db.Column(db.String(50))
    role =db.Column(db.String(20) ,default ='Influencer')
    flagged = db.Column(db.String(20) ,default='False')
    reason = db.Column(db.String(50))        
    platform = db.relationship('Social_media',backref = 'influencer')
    ad_request = db.relationship('Ad_request',backref = 'influencer',secondary ='association')
    
class Social_media(db.Model):
    influencer_id =  db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'),primary_key=True,autoincrement =True)
    Platform = db.Column(db.String(50), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)
     
class Sponsor(db.Model):
    sponsor_id = db.Column(db.Integer,primary_key=True,autoincrement =True)
    companyname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20)) 
    password = db.Column(db.String(50))
    role = db.Column(db.String(20) ,default='sponsor')
    flagged = db.Column(db.Boolean ,default=False)
    campaign = db.relationship('Campaign',backref='sponsor')
    
class Campaign(db.Model):
    sponsor_id = db.Column(db.Integer,db.ForeignKey('sponsor.sponsor_id'))
    campaign_id = db.Column(db.Integer,primary_key=True,autoincrement =True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    campaign_title = db.Column(db.String(20))
    category = db.Column(db.String(20))
    about = db.Column(db.String(100))
    status = db.Column(db.String(10))
    payment = db.Column(db.String(10) )
    payment_id = db.Column(db.Integer)
    flag = db.Column(db.Boolean ,default=False)
    
    request = db.relationship('Ad_request',backref='campaign')
        
class Ad_request(db.Model):
    ad_request_id = db.Column(db.Integer,primary_key=True,autoincrement =True)
    campaign_id = db.Column(db.Integer,db.ForeignKey('campaign.campaign_id'))
    Influencer_id = db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'))
    infl_username = db.Column(db.String(50),db.ForeignKey('influencer.username'))
    response = db.Column(db.String(20),default='False')
    followers = db.Column(db.Integer)
    remarks = db.Column(db.String(20))
    
class  Association(db.Model):
    Influencer_id = db.Column(db.Integer,db.ForeignKey('influencer.influencer_id'))
    ad_request_id = db.Column(db.Integer,db.ForeignKey('ad_request.ad_request_id'),primary_key=True)
    
