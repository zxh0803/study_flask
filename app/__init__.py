# coding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import current_user
from app import views,models
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
lm.login_view = 'login'

@app.before_request
def before_request():
    g.user = current_user