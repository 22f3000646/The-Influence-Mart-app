from flask import Flask,render_template,Blueprint,request,redirect,url_for
from config import Config 
from models import db,User
app=Flask(__name__)

app.config.from_object(Config)  # Load the configuration from Config class
db.init_app(app)

admin_bp=Blueprint("admin",__name__)
@admin_bp.route("/",methods=['GET','POST'])
def Admin():
    if request.method=='POST':
        user1=request.form['username']
        passw=request.form['password']
        user = User.query.filter_by(username=user1).first()
        if user and user.check_password(passw):
            return render_template("Admin dashboard.html",Admin=user.username)
        else:
             # Handle invalid credentials
            return f"Invalid credentials,{user.passw}", 401
        
    return render_template("Adminlogin.html")

@admin_bp.route("/dashboard")
def dashboard():
    return render_template("/admin dashboard.html")
@admin_bp.route("/find")
def dashboard1():
    return render_template("/admin_find.html")
@admin_bp.route("/stats")
def dashboard2():
    return render_template("/admin_stats.html")

