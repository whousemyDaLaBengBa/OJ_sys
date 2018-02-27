import sys
sys.path.append('/home/hscuabc/WorkSpace/python-web/OJ_sys')
from flask import session
from app import app as mainapp

mainapp.route('/sessiontest')
def add_user():
    session['username'] = 'session'
    session['nickname'] = 'session'
    session['password'] = 'session'
    return 'done'


mainapp.route('/sessionquery')
def que():
    str = session.get('username')+' '+session.get('nickname')+' '+session.get('password')
    return str