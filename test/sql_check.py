import sys
sys.path.append('/home/hscuabc/WorkSpace/python-web/OJ_sys')
from app.user import db,User


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

def add_user_by_number(st, en):
    for k in range(st, en):
        nuser = User(str(k), 'nickname', '123456', None,0)
        db.session.add(nuser)
    try:
        db.session.commit()
    except:
        return False
    else:
        return True

#que = User.query.filter_by(email='981944620@qq.com').first()
#print(que.password)
print(add_user_by_number(2016310200110,2016310200200))