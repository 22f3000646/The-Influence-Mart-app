from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/admin")
def Admin():
    return render_template("Adminlogin.html")
@app.route("/influencer")
def influencer():
    return render_template("influencer_login.html")
@app.route("/sponsor")
def sponsor():
    return render_template("sponsor login.html")
@app.route("/sponsor_registration")
def register1():
    return render_template("sponsor_registration.html")
@app.route("/register_influencer")
def register2():
    return render_template("/influencer_registration.html")
@app.route("/admin_dashboard")
def dash():
    return render_template("/base.html",user="akshay")

if __name__=="__main__":
    app.run(debug=True)
