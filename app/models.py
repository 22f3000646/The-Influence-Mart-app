from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Set your database URI here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Increased length to accommodate hashed password
    role = db.Column(db.String(20), nullable=False)
    
    def __init__(self, username, password, role):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.role = role

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

def add_user():
    with app.app_context():  # Ensure this runs within the app context
        db.create_all()  # Create tables if they don't exist
        if not User.query.filter_by(username='akshay').first():  # Check if user already exists
            user1 = User('akshay', 'asdfg', 'admin')
            db.session.add(user1)
            db.session.commit()

if __name__ == "__main__":
    add_user()  # Call the function to add a user
    app.run(debug=True)
