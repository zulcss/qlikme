from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
app.secret_key = 'this is really the key'

from qlikme import views
