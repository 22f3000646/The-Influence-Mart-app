from flask import render_template,Blueprint,request,session,redirect,url_for,flash
from models import *
from forms import sponsor_registration
sponsor=Blueprint("sponsor",__name__)
@sponsor.route("/")
def Login():
    if request.method == 'POST':
        user1=request.form['username']
        passw=request.form['password']
        user = Sponsor.query.filter_by(username=user1).first()
        if user and passw == bcrypt.gensalt(user.password).decode('utf-8'):
            session['user']=user.username
            return redirect(url_for('sponsor.dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('sponsor.Login'))
    return  redirect(url_for('sponsor.dashboard'))
@sponsor.route("/register", methods=['GET','POST'])
def register():
    form = sponsor_registration()
    if form.validate_on_submit():
        existing_username = Sponsor.query.filter_by(username =form.username.data).first()
        if existing_username:
            flash('username already exist')
            return render_template('influencer_registration.html',form=form)
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_sponsor = Sponsor(companyname =form.name.data,
                              username = form.username.data,
                              email = form.email.data,
                              phone = form.phone.data,
                              password = hashed_password)
        db.session.add(new_sponsor)
        db.session.commit()
        flash('account created successfully')
        return render_template("sponsor_registration.html",form=form)
    
    return render_template("sponsor_registration.html",form=form)
@sponsor.route("/dashboard")
def dashboard():
    return render_template("sponsor_profile.html")
