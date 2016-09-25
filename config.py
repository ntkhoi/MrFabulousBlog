# configuration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask.ext.misaka import Misaka

SQLALCHEMY_DATABASE_URI = 'sqlite:///MrFabulousBlog.db'
DEFAULT_FILE_STORAGE = 'filesystem'

#create application
app = Flask(__name__)
app.config.from_object( __name__)
db = SQLAlchemy(app)
Misaka(app)


