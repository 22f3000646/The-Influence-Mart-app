from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,DateField,TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class Registeration(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=8,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=20)])
    confirm_password = PasswordField('Confirm Password',validators =[DataRequired(),EqualTo('Password',message='both password should be same')])
    sub,it =SubmitField('Register')
    
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')
    
class CampaignForm(FlaskForm):
    campaign_title = StringField('Campaign Title',validators=[DataRequired(),Length(max=30)])
    category = StringField('Category',validators=[Length(max=10)])
    about = TextAreaField('About',validators=[DataRequired(),Length(max=100)])
    start_date = DateField('Start Date',format='%Y-%m-%d',validators=[DataRequired()])
    end_date = DateField('End Date',format='%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('Create Campaign')

class AdRequestForm(FlaskForm):
    campaign_id = IntegerField('Campaign ID',validators=[DataRequired()])
    influencer_id = IntegerField('Influencer ID',validators=[DataRequired()])
    followers = IntegerField('Followers',validators=[DataRequired()])
    remarks = TextAreaField('Remarks',validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit Ad Request')
    
    