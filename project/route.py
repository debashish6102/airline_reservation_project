from flask import Blueprint, render_template
from flask_login import login_required, current_user
views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home_page():
    return render_template("home.html",  user=current_user)


@views.route('/user_detail')
def user_detail_page():
    return render_template("user_detail.html", user=current_user)

@views.route('/flight_detail')
def flight_detail_page():
    return render_template("flight_detail.html", user=current_user)
