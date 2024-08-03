from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from admin import admin_bp
# from influencer import influencer_bp
# from sponsors import sponsor_bp
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
app.register_blueprint(admin_bp,url_prefix='/admin')
app.register_blueprint(influencer_bp,url_prefix='/influencer')
app.register_blueprint(sponsor_bp,url_prefix='/sponsor')
# app.config.from_object('config.Config')  # Load configuration from config.py
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


if __name__=='__main__':
    app.run(debug=True)