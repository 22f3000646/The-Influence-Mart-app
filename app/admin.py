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
    return render_template("/admin dashboard.html",Admin=user.username)
@adminbp.route("/find")
def dashboard1():
    if 'user' not in session:
        return redirect(url_for('Admin.Login'))
    return render_template("/admin_find.html")
@adminbp.route("/stats")
def dashboard2():
    if 'user' not in session:
        return redirect(url_for('Admin.Login'))
    return render_template("/admin_stats.html")


@adminbp.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('Admin.Login'))




