from flask import Flask,render_template,Blueprint,request,redirect,url_for,session,flash
from models import db,User
admin_bp=Blueprint("Admin",__name__)

admin_bp.secret_key='asdfg@12345t'
@admin_bp.route("/",methods=['GET','POST'])
def Admin():
    if request.method=='POST':
        user1=request.form['username']
        passw=request.form['password']
        user = User.query.filter_by(username=user1).first()
        if user and user.check_password(passw):
            session['user']=user.username
            return redirect(url_for('Admin.dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('Admin.Admin'))

            
    return render_template("Adminlogin.html")

@admin_bp.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('Admin.Admin'))
    
    user=User.query.filter_by(username=session['user']).first()
    return render_template("/admin dashboard.html",Admin=user.username)
@admin_bp.route("/find")
def dashboard1():
    if 'user' not in session:
        return redirect(url_for('Admin.Admin'))
    return render_template("/admin_find.html")
@admin_bp.route("/stats")
def dashboard2():
    if 'user' not in session:
        return redirect(url_for('Admin.Admin'))
    return render_template("/admin_stats.html")


@admin_bp.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('Admin.Admin'))




