from flask import render_template,Blueprint,request,session,redirect,url_for,flash
from models import *
from forms import sponsor_registration,CampaignForm
sponsor=Blueprint("sponsor",__name__)
@sponsor.route("/",methods = ['GET','POST'])
def Login():
    if request.method == 'POST':
        user1 = request.form['username']
        passw = request.form['password']
        user = Sponsor.query.filter_by(username=user1).first()
        
        if user and bcrypt.checkpw(passw.encode('utf-8'), user.password.encode('utf-8')):
            session['user'] = user.username
            return redirect(url_for('sponsor.dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('sponsor.Login'))
    return  render_template('sponsor login.html')
@sponsor.route("/register", methods=['GET','POST'])
def register():
    form = sponsor_registration()
    if form.validate_on_submit():
        existing_username = Sponsor.query.filter_by(username =form.username.data).first()
        if existing_username:
            flash('username already exist')
            return render_template('sponsor_registration.html',form=form)
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
    if 'user' not in session:
        return redirect(url_for('sponsor.Login'))
    sponsor = Sponsor.query.filter_by(username=session['user']).first()
    return render_template("sponsor_profile.html",Sponsor = sponsor)

@sponsor.route('/campaigns')
def campaigns():
    if 'user' not in session:
        return redirect(url_for('sponsor.Login'))
    return render_template('sponsor_campaigns.html')

@sponsor.route('/add_campaigns', methods=['GET', 'POST'])
def campaign():
    if 'user' not in session:
        return redirect(url_for('sponsor.Login'))
    sponsor = Sponsor.query.filter_by(username=session['user']).first()
    form = CampaignForm()
    if form.validate_on_submit():
        campaign_title = form.campaign_title.data
        category = form.category.data
        about = form.about.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        
        new_campaign = Campaign(
            sponsor_id =sponsor.sponsor_id,
            campaign_title=campaign_title,
            category=category,
            about=about,
            start_date=start_date,
            end_date=end_date,
            status='active',  
            flag=False        
        )
        
        # Add to database and commit
        db.session.add(new_campaign)
        db.session.commit()
        
        return redirect(url_for('sponsor.campaigns'))
    
    return render_template('add_campaign.html', form=form)
@sponsor.route('/find')
def find():
    if 'user' not in session:
        return redirect(url_for('sponsor.Login'))
    return render_template('sponsor_find.html')

@sponsor.route('/stats')
def sponsor_stats():
    if 'user' not in session:
        return redirect(url_for('sponsor.Login'))
    total_sponsors = Sponsor.query.count()
    active_sponsors = Sponsor.query.filter_by(flagged=False).count()
    flagged_sponsors = Sponsor.query.filter_by(flagged=True).count()
    active_campaigns = Campaign.query.filter_by(status='active').count()
    completed_campaigns = Campaign.query.filter_by(status='completed').count()

    return render_template('sponsor_stats.html', 
                           total_sponsors=total_sponsors,
                           active_sponsors=active_sponsors,
                           flagged_sponsors=flagged_sponsors,
                           active_campaigns=active_campaigns,
                           completed_campaigns=completed_campaigns)
    
    
@sponsor.route('/logout')
def Logout():
    session.pop('user',None)
    return redirect(url_for('sponsor.Login'))
