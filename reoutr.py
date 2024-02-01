from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/login")
def login():
    return render_template('login.hmtl')

@app.route("/profile")
def profile():
    return render_template('profile.html')