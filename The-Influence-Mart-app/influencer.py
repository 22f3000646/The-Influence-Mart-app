from flask import Flask,render_template,Blueprint
influencer_bp=Blueprint("influencer",__name__)
@influencer_bp.route("/")
def influencer():
    return render_template("influencer_login.html")
@influencer_bp.route("/register")
def register():
    return render_template("/influencer_registration.html")