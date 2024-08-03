from flask import render_template,Blueprint
sponsor_bp=Blueprint("sponsor",__name__)
@sponsor_bp.route("/")
def sponsor():
    return render_template("sponsor login.html")
@sponsor_bp.route("/register")
def register():
    return render_template("sponsor_registration.html")
