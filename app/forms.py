from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,DateField,TextAreaField,IntegerField,BooleanField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class Registeration(FlaskForm):
    full_name = StringField('Username',validators=[DataRequired(),Length(min=4,max=20)]) 
    username = StringField('Username',validators=[DataRequired(),Length(min=8,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    niche = StringField('Niche', validators=[DataRequired()])
    platform = StringField('Platform') 
    follower_count = IntegerField('Follower Count') 
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=20)])
    confirm_password = PasswordField('Confirm Password',validators =[DataRequired(),EqualTo('password',message='both password should be same')])
    submit =SubmitField('Register')

class sponsor_registration(FlaskForm):
    name = StringField('name',validators=[DataRequired(),Length(min=4,max=20)])
    username = StringField('Username',validators=[DataRequired(),Length(min=8,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=20)])
    iAgree = BooleanField('I agree to the terms and conditions', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators =[DataRequired(),EqualTo('password',message='both password should be same')])    
    submit =SubmitField('Sign up')
class CampaignForm(FlaskForm):
    campaign_title = StringField('campaign Title',validators=[DataRequired(),Length(max=30)])
    category = StringField('category',validators=[Length(max=10)])
    about = TextAreaField('about',validators=[DataRequired(),Length(max=100)])
    start_date = DateField('start Date',format='%Y-%m-%d',validators=[DataRequired()])
    end_date = DateField('end Date',format='%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('create Campaign')

class AdRequestForm(FlaskForm):
    campaign_id = IntegerField('Campaign ID',validators=[DataRequired()])
    influencer_id = IntegerField('Influencer ID',validators=[DataRequired()])
    followers = IntegerField('Followers',validators=[DataRequired()])
    remarks = TextAreaField('Remarks',validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit Ad Request')
    
    