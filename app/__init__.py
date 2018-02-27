from flask import Flask
from flask_script import Manager
import app.config as config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['PERMANENT_SESSION_LIFETIME'] = 30*24*3600
app.debug = True
manger = Manager(app)