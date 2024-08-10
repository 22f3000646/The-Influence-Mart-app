from flask import Flask,render_template,Blueprint,request,redirect,url_for,session,flash
from models import *
admin=Blueprint("Admin",__name__)

admin.secret_key='asdfg@12345t'
@admin.route("/",methods=['GET','POST'])
def Admin():
    if request.method=='POST':
        user1=request.form['username']
        passw=request.form['password']
        user = Admin.query.filter_by(username=user1).first()
        if user and user.check_password(passw):
            session['user']=user.username
            return redirect(url_for('Admin.dashboard'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('Admin.Admin'))

            
    return render_template("Adminlogin.html")

@admin.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('Admin.Admin'))
    
    user=User.query.filter_by(username=session['user']).first()
    return render_template("/admin dashboard.html",Admin=user.username)
@admin.route("/find")
def dashboard1():
    if 'user' not in session:
        return redirect(url_for('Admin.Admin'))
    return render_template("/admin_find.html")
@admin.route("/stats")
def dashboard2():
    if 'user' not in session:
        return redirect(url_for('Admin.Admin'))
    return render_template("/admin_stats.html")


@admin.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('Admin.Admin'))




