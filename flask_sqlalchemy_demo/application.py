from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from app import app

"""flask_sqlalchemy模块的应用"""

# 创建db对象
db = SQLAlchemy(app)


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


def insert():
    author = Author(name='jack', age=23, gender=False)
    new = New(tag='热点', context='国家主席在全国文代会上发表重要讲话')
    author.new.append(new)
    db.session.add(author)
    db.session.commit()

def one_select():
    """单表查询,不需要session对象"""
    val = Author.query.all()
    print(val)

    val = Author.query.first()
    print(val)


def many_select():
    """多表查询需要session对象"""
    val = db.session.query(Author.name, New.tag).join(New, Author.id==New.author_id).all()
    print(val)


def update():
    """更新数据"""
    val = Author.query.filter(Author.id==2).first()
    print(type(val))
    val.name = 'Tom'
    val.age = 25
    val.gender = True
    db.session.commit()

def delete():
    """删除对象"""
    val = Author.query.filter(Author.id==2).first()
    db.session.delete(val)
    db.session.commit()

if __name__ == "__main__":
    db.drop_all()   # 删除表
    # db.create_all()     # 创建表

    # insert()

    # one_select()
    # many_select()
    # update()
    # delete()
    pass
