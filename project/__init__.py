from datetime import datetime
from flask import Flask, render_template, request, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite////tmp/test.db'
db = SQLAlchemy(app)

from project import route