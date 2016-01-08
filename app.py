from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static')

app.debug = True
app.config.from_object('settings')
db = SQLAlchemy(app)


import main.models
import main.views
