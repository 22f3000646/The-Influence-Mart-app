from flask import Flask,render_template
from admin import adminbp
from influencer import influencer
from sponsors import sponsor
from config import Config 
from models import db
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.secret_key='asdfg@12345t'
@app.route("/")
def home():
    return render_template("home.html")
app.register_blueprint(adminbp,url_prefix='/admin')
app.register_blueprint(influencer,url_prefix='/influencer')
app.register_blueprint(sponsor,url_prefix='/sponsor')

if __name__=='__main__':
    app.run(debug=True)



