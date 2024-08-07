from flask import Flask,render_template,Blueprint,request
influencer_bp=Blueprint("influencer",__name__)
@influencer_bp.route("/",methods=['GET','POST'])
def influencer():
    if request.method=='POST':
        name=request.form['fullName']
        user=request.form["username"]
        email=request.form["email"]
        phone=request.form["phone"]
        social_media = request.form.getlist('social_media[]')
        
        # Get the number of YouTube followers (this will be a string)
        youtube_followers = request.form.get('youtube_followers', '')
        instagram_followers=request.form["social_media[instagram_followers]"]
        facebook_followers=request.form["social_media[facebook_followers]"]
        snapchat_followers=request.form["social_media[snapchat_followers]"]
        # Process the data (convert to integer if needed)
        if youtube_followers:
            youtube_followers = int(youtube_followers)    
        if instagram_followers:
            instagram_followers = int(instagram_followers)
        if  facebook_followers:
            facebook_followers = int(facebook_followers)
        if  snapchat_followers:
            snapchat_followers = int(snapchat_followers)   
    
    return render_template("influencer_login.html")
@influencer_bp.route("/register")
def register():
    return render_template("/influencer_registration.html")