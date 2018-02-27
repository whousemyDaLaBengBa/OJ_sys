from app import app
from flask import request, render_template,session,redirect
from app.user import db, User, add_user, check_username


def add_user_by_number(st, en):#function tested
    en = en + 1
    for k in range(st, en):
        if (check_username(str(k))):
            nuser = User(str(k), 'nickname', '123456', None,0)
            db.session.add(nuser)
    try:
        db.session.commit()
    except:
        return False
    else:
        return True


#reset
def reset_password(name):#function tested
    que_e = User.query.filter_by(email=name).first()
    que_n = User.query.filter_by(username=name).first()
    if que_e != None:
        User.query.filter_by(email=name).update({'password': '123456'})

    if que_n != None:
        User.query.filter_by(username=name).update({'password': '123456'})
    db.session.commit()


#delete
def delete_user(name):#function tested
    que_e = User.query.filter_by(email=name).first()
    que_n = User.query.filter_by(username=name).first()
    if que_e != None:
        User.query.filter_by(email=name).delete()

    if que_n != None:
        User.query.filter_by(username=name).delete()
    db.session.commit()


@app.route('/admin')
def admin():
    try:
        username = session['username']
        nickname = session['nickname']
        isAdmin = session['isAdmin']
    except:
        return 'Access Violation Please Login first'
    else:
        if isAdmin == 1:
            return render_template('admin.html',username = username,nickname = nickname,isAdmin = isAdmin)
        else:
            return 'Access Violation'


@app.route('/admin/addmultiuser',methods = ['GET','POST'])#untested按数字从小到大添加多个用户
def addmultiuser():
    st = request.values.get('st')
    en = request.values.get('en')
    if add_user_by_number(st, en) == True:
        return 'add successfully'
    else:
        return 'add failed please try again'


@app.route('/admin/adduser', methods = ['GET','POST'])
def adduser():
    print('begin')
    try:
        print('try')
        name = request.values.get('username')
        password = request.values.get('password')
        isAdmin = request.valuse.get('isAdmin')
        print(name)
        print(password)
        print(isAdmin)
    except:
        print('except')
        return 'Access Violation'
    else:
        print('else')
        try:
            print(name)
            print(password)
            print(isAdmin)
            if isAdmin == 'on':
                add_user(name, None, password, None, 1)
                print('11111')
            else:
                add_user(name, None, password, None, 0)
                print(00000)
        except:
            return 'Unknow error'
        else:
            return redirect('/admin')



@app.route('/admin/reset', methods = ['GET', 'POST'])
def reset():
    try:
        name = request.values.get('username')
    except:
        return 'Access Violation'
    else:
        reset_password(name)







@app.route('/admin/delete', methods = ['GET', 'POST'])
def delete():
    try:
        name = request.values.get('username')
    except:
        return 'Access Violation'
    else:
        delete_user(name)