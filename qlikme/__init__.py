from flask import Flask

app = Flask(__name__)
app.secret_key = 'this is really the key'

from qlikme import views
