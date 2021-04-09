from project import app
from flask import render_template
@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/user_detail')
def user_detail_page():
    return render_template("user_detail.html")

@app.route('/login')
def login_page():
    return render_template("login.html")
