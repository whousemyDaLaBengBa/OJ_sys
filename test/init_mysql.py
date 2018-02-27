import sys
sys.path.append('/home/hscuabc/WorkSpace/python-web/OJ_sys')
from app.user import db,User

db.create_all()
admin = User('admin', '管理员不需要昵称', 'z7895123xb^', '3197235088@qq.com', 1)
db.session.add(admin)
db.session.commit()