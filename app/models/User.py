import re
import json
from ..extensions import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50),nullable=False)

    @classmethod
    def is_username_available(cls,username):

        if username is None:
            return json.dumps({'code':201,'msg':"用户名不能为空"},ensure_ascii=False)
        elif not bool(re.match(r"^[a-zA-Z0-9]+$",username)):#匹配用户名仅拥有字母和数字
            return json.dumps({'code':202,'msg':"用户名只能为字母和数字"},ensure_ascii=False)
        else:
            return 200

    @classmethod
    def adduser(cls, username, password):
        try:
            print("try")
            code = cls.is_username_available(username)
            if code == 200:
                user = cls(username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return json.dumps({'code':200,'msg':"用户添加成功！"},ensure_ascii=False)
            else:
                return code
        except Exception as e:
            db.session.rollback()
            return json.dumps({'code':500,'msg':f"数据库未知错误+{e}"},ensure_ascii=False)


