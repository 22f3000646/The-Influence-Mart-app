from flask import Flask, render_template, Blueprint, request,flash,session,redirect,url_for
from models import db, Influencer,User
influencer=Blueprint("influencer",__name__)
influencer.secret_key='asdfg@12345t'
@influencer.route('/',methods=['GET','POST'])
def Influencer():
    if request.method == 'POST':
        user1=request.form['username']
        passw=request.form['password']
        user = User.query.filter_by(username=user1).first()
        if user and user.check_password(passw):
            session['user']=user.username
            return redirect(url_for('influencer.dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('influencer.influencer'))
        

@influencer.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['fullName']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        social_media = request.form.getlist('social_media[]')
        social_media_str = ','.join(social_media)
        youtube_followers = request.form.get('youtube_followers', '')
        instagram_followers = request.form.get('instagram_followers', '')
        facebook_followers = request.form.get('facebook_followers', '')
        snapchat_followers = request.form.get('snapchat_followers', '')
        if youtube_followers:
            youtube_followers = int(youtube_followers)
        if instagram_followers:
            instagram_followers = int(instagram_followers)
        if facebook_followers:
            facebook_followers = int(facebook_followers)
        if snapchat_followers:
            snapchat_followers = int(snapchat_followers)
        category = request.form.get('category', '')
        number = request.form.get('followers', '')
        bio = request.form.get('bio', '')

        user = Influencer(full_name=name,username=username,email=email,phone=phone,
                          platform=social_media_str,insta=instagram_followers,youtube=youtube_followers,
                          facebook=facebook_followers,snapchat=snapchat_followers,niche=category,
                          followers=number,bio=bio)
        db.session.add(user)
        db.session.commit()
        flash('Account created succesfully')
        return render_template('influencer_login.html')
    return render_template('influencer_registration.html')

@influencer.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('influencer.influencer'))
    user=User.query.filter_by(username=session['user']).first()
    user=User.query.filter_by(username=session['user']).first()
    return render_template("/influencer_dashboard.html")



