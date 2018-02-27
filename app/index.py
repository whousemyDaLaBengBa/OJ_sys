import os.path as rp
path = rp.realpath(__file__)
path = path[0:-12]
import sys
sys.path.append(path)
from flask import render_template,session
from app import app as mainapp
from app import manger
from app.user import register,log_in_out,admin_operation


@mainapp.route('/')
def index():
    try:
        username = session['username']
        nickname = session['nickname']
        isAdmin = session['isAdmin']
    except:
        return render_template('welcome.html')
    else:
        return render_template('welcome.html',username = username, nickname = nickname,isAdmin=isAdmin)

if __name__ == '__main__':
    manger.run()

