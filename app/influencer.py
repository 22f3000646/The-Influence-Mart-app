from flask import Flask, render_template, Blueprint, request, flash, session, redirect, url_for
from models import *
import bcrypt
from forms import Registeration

influencer = Blueprint("influencer", __name__)

@influencer.route('/', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        user1 = request.form['username']
        passw = request.form['password']
        user = Influencer.query.filter_by(username=user1).first()

        if user and bcrypt.checkpw(passw.encode('utf-8'), user.password.encode('utf-8')):
            session['user'] = user.username
            return redirect(url_for('influencer.dashboard'))
        else:
            flash('Invalid Credentials', 'error')
            return redirect(url_for('influencer.Login'))

    return render_template('influencer_login.html')

@influencer.route("/registration", methods=['GET', 'POST'])
def registration():
    form = Registeration()
    if form.validate_on_submit():
        existing_username = Influencer.query.filter_by(username=form.username.data).first()

        if existing_username:
            flash('Username already exists', 'error')
            return render_template('influencer_registration.html', form=form)

        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_influencer = Influencer(
            full_name=form.full_name.data,
            username=form.username.data,
            password=hashed_password,
            email=form.email.data,
            phone=form.phone.data,
            bio=form.bio.data,
            niche=form.niche.data
        )

        db.session.add(new_influencer)
        db.session.commit()

        flash('Account created successfully', 'success')
        return redirect(url_for('influencer.Login'))

    return render_template('influencer_registration.html', form=form)

@influencer.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('influencer.Login'))

    user = Influencer.query.filter_by(username=session['user']).first()
    influencer = Influencer.query.filter_by(username=user.username).first_or_404()

    
    # Render the dashboard template with the influencer and campaigns data
    return render_template('influencer_dashboard.html', influencer=influencer)

@influencer.route('/campaigns')
def campaigns():
    if 'user' not in session:
        return redirect(url_for('influencer.Login'))

    user = Influencer.query.filter_by(username=session['user']).first()
    influencer = Influencer.query.filter_by(username=user.username).first_or_404()
    ad_requests = Ad_request.query.filter_by(Influencer_id=influencer.influencer_id).all()
    campaign_ids = [ad_request.campaign_id for ad_request in ad_requests]
    campaigns = Campaign.query.filter(Campaign.campaign_id.in_(campaign_ids)).all()
    
    return render_template('influencer_campaigns.html', campaigns=campaigns,influencer=influencer)

@influencer.route('/send_ad_request/<int:campaign_id>', methods=['POST'])
def send_ad_request(campaign_id):
    if 'user' not in session:
        return redirect(url_for('influencer.Login'))

    user = Influencer.query.filter_by(username=session['user']).first()
    influencer = Influencer.query.filter_by(username=user.username).first_or_404()

    # Ensure the user is an influencer
    if user.role != 'Influencer':
        flash('You do not have permission to perform this action.', 'warning')
        return redirect(url_for('home'))  # Redirect to home or another appropriate page

    # Query the influencer data based on the current user
    influencer = Influencer.query.filter_by(username=user.username).first_or_404()

    # Get remarks from the form
    remarks = request.form.get('remarks')

    # Create a new ad request
    new_ad_request = Ad_request(
        campaign_id=campaign_id,
        Influencer_id=influencer.influencer_id,
        infl_username=influencer.username,
        response='Pending',
        followers=None,  # You can set this as needed
        remarks=remarks
    )

    # Add and commit to the database
    db.session.add(new_ad_request)
    db.session.commit()

    flash('Ad request sent successfully!', 'success')
    return redirect(url_for('influencer.dashboard'))

@influencer.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('influencer.Login'))

    