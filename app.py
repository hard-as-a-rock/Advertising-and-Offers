from flask import Flask, g

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user


app = Flask(__name__, static_url_path='/static')


app.debug = True
app.config.from_object('settings')
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.before_request
def before_request():
    g.user = current_user

import main.views