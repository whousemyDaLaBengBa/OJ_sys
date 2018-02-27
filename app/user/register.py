from app import app
from flask import request, render_template,session
from app.user import db, User, add_in_session, check_email, check_username, add_user


@app.route('/register')
def register():
    name = request.args.get('checkname')
    if name != None:
        if check_username(name) == True:
            return "true"
        else:
            return 'false'

    mail = request.args.get('checkemail')
    if mail != None:
        if check_email(mail) == True:
            return "true"
        else:
            return 'false'
    return render_template('register.html')


@app.route('/register',methods=['POST','GET'])
def registeraction():
    try:
        name = request.values.get('username')
        email = request.values.get('email')
        nickname = request.values.get('nickname')
        password = request.values.get('password')
        add_user(name, nickname, password, email, 0)
    except:
        return 'false'
    else:
        add_in_session(name,nickname,0)
        return 'true'