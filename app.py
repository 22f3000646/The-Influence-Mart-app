from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = "John Doe"
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
