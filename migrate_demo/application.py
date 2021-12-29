import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from app import db

"""
flask-migrate模块的应用
1、同步表结构
2、flask db init
3、flask db migrate
4、flask db upgrade
"""


class Author(db.Model):
    __tablename__ = 't_author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Boolean)

    createTime = db.Column(db.DateTime, default=datetime.now)
    updateTime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<id:{self.id}, name:{self.name}, age:{self.age}, gender:{self.gender}>"


class New(db.Model):
    __tablename__ = "t_new"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(10), nullable=False)
    context = db.Column(db.String(100))
    createTime = db.Column(db.DateTime, default=datetime.now)
    updateTime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # 创建外键
    author_id = db.Column(db.Integer, db.ForeignKey('t_author.id'))

    # 创建互相查找
    authorInfo = db.relationship('Author', backref='new')

    def __repr__(self):
        return f"<id:{self.id}, tag:{self.tag}, context:{self.context}, authorID:{self.author_id}>"


if __name__ == "__main__":
    db.drop_all()
