from flask import Flask,render_template,Blueprint
admin_bp=Blueprint("admin",__name__)
@admin_bp.route("/")
def Admin():
    return render_template("Adminlogin.html")
@admin_bp.route("/dashboard")
def dashboard():
    return render_template("/admin dashboard.html",Admin="akshay")
@admin_bp.route("/find")
def dashboard1():
    return render_template("/admin_find.html",Admin="akshay")
@admin_bp.route("/stats")
def dashboard2():
    return render_template("/admin_stats.html",Admin="akshay")
