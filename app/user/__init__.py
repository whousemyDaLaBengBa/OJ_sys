from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from app.config import MYSQL_NAME,MYSQL_PASS,MYSQL_USER_TABLE
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + MYSQL_NAME + ':' + MYSQL_PASS + '@localhost/' + MYSQL_USER_TABLE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_charset': 'utf8'}
    username = db.Column(db.String(80), primary_key=True)
    nickname = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=False)
    isAdmin = db.Column(db.Boolean, unique=False)

    def __init__(self, username, nickname,password, email, isAdmin):
        self.username = username
        self.nickname = nickname
        self.email = email
        self.password = password
        self.isAdmin = isAdmin

    def __repr__(self):
        return '<User %r>' % self.username


def add_in_session(username,nickname,isAdmin):
    session['username'] = username
    session['nickname'] = nickname
    session['isAdmin'] = isAdmin


def check_username(name):
    que = User.query.filter_by(username=name).first()
    if que == None:
        return True
    else:
        return False


def check_email(emai):
    que = User.query.filter_by(email=emai).first()
    if que == None:
        return True
    else:
        return False

def add_user(name, nickname, password, email, isadmin):
    nuser = User(name, nickname, password , email, isadmin)
    db.session.add(nuser)
    db.session.commit()