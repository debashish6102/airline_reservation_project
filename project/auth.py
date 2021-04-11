from flask import Blueprint, render_template, request, flash, url_for, redirect
from . import db
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        user1 = User.query.filter_by(user_name=user_name).first()
        user = User.query.filter_by(email=user_name).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home_page'))
            else:
                flash('Incorrect password, try again.', category='error')
        elif user1:
            if check_password_hash(user1.password_hash, password):
                flash('Logged in successfully!', category='success')
                login_user(user1, remember=True)
                return redirect(url_for('views.home_page'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email or username does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home_page'))


@auth.route('/user_detail', methods=['GET', 'POST'])
def user_detail_page():
    spec_symbols = ['$', '@', '#', '%', '!', '*']
    if request.method == 'POST':
        fname = request.form.get('fname')
        mname = request.form.get('mname')
        lname = request.form.get('lname')
        user_sex = request.form.get('user_sex')
        phone = request.form.get('phone')
        email = request.form.get('email')
        adhaar = request.form.get('adhaar')
        user_name = request.form.get('user_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        user1 = User.query.filter_by(user_name=user_name).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(email) < 4:
            flash('email must be greater than 3 character ', category='error')
        elif len(phone) < 10:
            flash('phone number should be of 10 digits', category='error')
        elif len(adhaar) < 12:
            flash('adhaar number should be 12 digit long', category='error')
        elif len(user_name) < 2:
            flash(' user id should be  greater than 2 digits', category='error')
        elif user1:
            flash('error user name already exist', category='error')
        elif len(password1) < 6:
            flash('error lenght should be at least 6', category='error')
        elif len(password1) > 16:
            flash('error lenght should not be more than 16', category='error')
        elif not any(x.isdigit() for x in password1):
            flash('error password should have one numeral', category='error')
        elif not any(x.isupper() for x in password1):
            flash('error password should have one upper digit', category='error')
        elif not any(x.islower() for x in password1):
            flash('error password should have one lower digit', category='error')
        elif not any(x in spec_symbols for x in password1):
            flash('error password should have one special symbol(!,@,#,$,%,*)', category='error')
        else:
            new_user = User(fname=fname, mname=mname, lname=lname, sex=user_sex, phone=phone, email=email,
                            adhaar=adhaar, password_hash=generate_password_hash(
                    password1, method='sha256'), city_id=0, user_name=user_name)
            db.session.add(new_user)
            db.session.commit()
            #login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home_page'))
    return render_template("user_detail.html", user=current_user)
