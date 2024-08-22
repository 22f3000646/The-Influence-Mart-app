from flask import Flask,render_template,Blueprint,request,redirect,url_for,session,flash
from models import *
adminbp=Blueprint("Admin",__name__)

@adminbp.route("/",methods=['GET','POST'])
def Login():
        if request.method=='POST':
            user1=request.form['username']
            passw=request.form['password']
            user = Admin.query.filter_by(username=user1).first()
            if user and user.check_password(passw):
                session['user']=user.username
                return redirect(url_for('Admin.dashboard'))
            else:
                flash('Invalid Credentials')
                return redirect(url_for('Admin.Login'))

        return render_template("Adminlogin.html")

@adminbp.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('Admin.Login'))
    user=Admin.query.filter_by(username=session['user']).first()
    active_influencers_count =Influencer.query.count()
    campaigns_count = Campaign.query.count()
    active_sponsors_count = Sponsor.query.count()
    ad_requests_count= Ad_request.query.count()
    flagged_users= Influencer.query.filter_by(flagged='True').all()
    flagged_campaigns= Campaign.query.filter_by(status='flagged').all()
    return render_template("/admin dashboard.html",Admin='akshay',
                           active_influencers_count=active_influencers_count,
                           active_sponsors_count=active_sponsors_count,
                           campaigns_count=campaigns_count,
                           ad_requests_count=ad_requests_count,
                           flagged_users = flagged_users,
                           flagged_campaigns =flagged_campaigns 
                           )

    
@adminbp.route("/find",methods=['GET','POST'])
def dashboard1():
    if 'user' not in session:
        return redirect(url_for('Admin.Login'))
    search = request.form.get('search','')
    if request.method == 'POST':
        sponsors = Sponsor.query.filter(Sponsor.companyname.like(f'%{search}%')).all()
        campaigns = Campaign.query.filter(Campaign.campaign_title.like(f'%{search}%')).all()
        influencers = Influencer.query.filter(Influencer.username.like(f'%{search}%')).all()
        return render_template('admin_find.html',sponsors=sponsors,campaigns=campaigns,influencers=influencers,search=search)
    return render_template("/admin_find.html")
@adminbp.route("/stats")
def dashboard2():
    if 'user' not in session:
        return redirect(url_for('Admin.Login'))
    ad_requests_count= Ad_request.query.count()
    campaigns_count = Campaign.query.count()
    active_influencers_count =Influencer.query.count()
    active_sponsors_count=Sponsor.query.filter_by(flagged='False').count()
    inactive_sponsors_count=Sponsor.query.filter_by(flagged='True').count()
    flagged_sponsors_count=Sponsor.query.filter_by(flagged='True').count()
    flagged_influencers_count = Influencer.query.filter_by(flagged='True').count()
    active_campaigns_count=Campaign.query.filter_by(status='Active').count()
    completed_campaigns_count=Campaign.query.filter_by(status='Completed').count()

    return render_template('admin_stats.html',active_sponsors_count=active_sponsors_count,
                        inactive_sponsors_count=inactive_sponsors_count,
                        flagged_sponsors_count=flagged_sponsors_count,
                        active_campaigns_count=active_campaigns_count,
                        completed_campaigns_count=completed_campaigns_count,
                        flagged_influencers_count =flagged_influencers_count ,
                        ad_requests_count = ad_requests_count,
                        campaigns_count = campaigns_count,
                        active_influencers_count = active_influencers_count)
    

@adminbp.route('/flag_sponsor/<int:sponsor_id>', methods=['POST'])
def flag_sponsor(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    sponsor.flagged =True
    db.session.commit()
    flash('Sponsor has been flagged.')
    return redirect(url_for('Admin.dashboard1'))

@adminbp.route('/flag_campaign/<int:campaign_id>', methods=['POST'])
def flag_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    campaign.flagged =True
    db.session.commit()
    flash('Campaign has been flagged.')
    return redirect(url_for('Admin.dashboard1'))

@adminbp.route('/flag_influencer/<int:influencer_id>',methods=['POST'])
def flag_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    influencer.flagged =True
    db.session.commit()
    flash('Influencer has been flagged.')
    return redirect(url_for('Admin.dashboard1'))

@adminbp.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('Admin.Login'))




