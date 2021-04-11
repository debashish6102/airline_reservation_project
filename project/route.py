from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home_page():
    return render_template("home.html")


@views.route('/user_detail')
def user_detail_page():
    return render_template("user_detail.html")


