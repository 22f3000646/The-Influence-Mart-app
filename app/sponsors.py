from flask import render_template,Blueprint
sponsor=Blueprint("sponsor",__name__)
@sponsor.route("/")
def Sponsor():
    return render_template("sponsor login.html")
@sponsor.route("/register")
def register():
    return render_template("sponsor_registration.html")
@sponsor.route("/profile")
def profile():
    return render_template("sponsor_profile.html")
