# from flask import Flask,render_template,Blueprint,request,redirect,url_for
# from config import Config 
# from models import db, User 
# app=Flask(__name__)

# app.config.from_object(Config)  # Load the configuration from Config class
# db.init_app(app)

# admin_bp=Blueprint("admin",__name__)
# @admin_bp.route("/",methods=['GET','POST'])
# def Admin():
#     if request.method=='POST':
#         username=request.form['username']
#         password=request.form['password']
#         user = User.query.filter_by(username=username, password=password).first()
#         if user:
#                 return render_template("Admin dashboard.html")
#         else:
#                 # Handle invalid credentials
#                 pass
        
#     return render_template("Adminlogin.html")
    
# @admin_bp.route("/dashboard")
# def dashboard():
#     return render_template("/admin dashboard.html")
# @admin_bp.route("/find")
# def dashboard1():
#     return render_template("/admin_find.html")
# @admin_bp.route("/stats")
# def dashboard2():
#     return render_template("/admin_stats.html")

# app.register_blueprint(admin_bp)

# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, render_template, Blueprint, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    
    def __init__(self, username, password, role):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.role = role

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Create tables if they don't exist
with app.app_context():
    db.create_all()

    # Add a user if not already present
    if not User.query.filter_by(username='akshay').first():
        user1 = User('akshay', 'asdfg', 'admin')
        db.session.add(user1)
        db.session.commit()

# Define a blueprint for admin routes
admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return render_template("Admin dashboard.html")
        else:
            # Handle invalid credentials
            return "Invalid credentials", 401
        
    return render_template("Adminlogin.html")

@admin_bp.route("/dashboard")
def dashboard():
    return render_template("admin_dashboard.html")

@admin_bp.route("/find")
def find():
    return render_template("admin_find.html")

@admin_bp.route("/stats")
def stats():
    return render_template("admin_stats.html")

# Register the blueprint
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
