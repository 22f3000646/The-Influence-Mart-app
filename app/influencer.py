from flask import Flask, render_template, Blueprint, request,flash,session,redirect,url_for
from models import *
influencer=Blueprint("influencer",__name__)
import bcrypt
from forms import Registeration
@influencer.route('/',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        user1=request.form['username']
        passw=request.form['password']
        user = Influencer.query.filter_by(username=user1).first()
        if user and passw == bcrypt.gensalt(user.password).decode('utf-8'):
            session['user']=user.username
            return redirect(url_for('influencer.dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('influencer.Login'))
    return render_template('influencer_login.html')
        

@influencer.route("/registration", methods=['GET', 'POST'])
def registration():
    form = Registeration()
    if form.validate_on_submit():
            existing_username = Influencer.query.filter_by(username =form.username.data).first()
            if existing_username:
                flash('username already exist')
                return render_template('influencer_registration.html',form=form)
            hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            new_influencer = Influencer(full_name=form.full_name.data,
            username=form.username.data,
            password=hashed_password,
            email= form.email.data,
            phone=form.phone.data,
            bio=form.bio.data,
            niche=form.niche.data)
              
            db.session.add(new_influencer)
            db.session.commit()
            flash('Account created succesfully')
            return render_template('sponsor_registration.html',form=form)
    
    return render_template('sponsor_registration.html',form=form)

@influencer.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('influencer.Login'))
    user=Influencer.query.filter_by(username=session['user']).first()
    user=Influencer.query.filter_by(username=session['user']).first()
    return render_template("/influencer_dashboard.html")



