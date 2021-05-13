from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path, environ
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .route import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .model import User, Airport, Flight, Passenger, Booking_details

    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'views.home_page'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('project/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
