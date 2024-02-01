from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/admin")
def admin():
    return render_template('admin.html', items = ['user1', 'user2'])

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print("heyy")
        if request.form['usernme'] == "admin":
            if request.form['password'] == '123456':
                print(request.form['usernme'])
                return "hii"
            else:
                return "Wrong password"
        else:
            return "waitt"

@app.route("/profile")
def profile():
    return render_template('profile.html', items = [['amazon.com', 'user1', '123'],
                                                    ['facebook.com', 'user2', '456']])