from app import app
from flask import request, session, redirect
from app.user import User,add_in_session


#untested



def login_check_add(name, passw):
    username = User.query.filter_by(username=name).first()
    email = User.query.filter_by(email = name).first()

    if (username != None) and (username.password==passw):
        name = username.username
        nickname = username.nickname
        isAdmin = username.isAdmin
        add_in_session(name,nickname,isAdmin)
        return True
    elif (email != None) and (email.password == passw):
        name = email.username
        nickname = email.nickname
        isAdmin = email.isAdmin
        add_in_session(name, nickname, isAdmin)
        return True
    else:
        return False


@app.route('/login',methods = ['POST','GET'])#someting wrong
def login():
    try:
        username = request.values.get('username')
        password = request.values.get('password')
    except:
        return 'Access Violation'
    else:
        if login_check_add(username, password) == 1:
            return redirect('/')
        else:
            return 'login failed'


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
