from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = '027f5ce927ba58e1709c9942adb5f5a9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
