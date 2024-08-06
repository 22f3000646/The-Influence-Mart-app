from flask import Flask,render_template
from admin import admin_bp
from influencer import influencer_bp
from sponsors import sponsor_bp
from models import db,User
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
@app.route("/")
def home():
    return render_template("home.html")
app.register_blueprint(admin_bp,url_prefix='/admin')
app.register_blueprint(influencer_bp,url_prefix='/influencer')
app.register_blueprint(sponsor_bp,url_prefix='/sponsor')

if __name__=='__main__':
    app.run(debug=True)



