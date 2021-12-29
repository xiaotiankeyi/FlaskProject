import random
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DATETIME, TEXT
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy_demo.db_tool import Base, engine

"""
实现数据的分组和分组后的过滤group_by,having
"""

Session = sessionmaker(engine)


class NewAuthor(Base):
    """新闻作者表"""
    __tablename__ = "newAuthor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    gender = Column(Boolean)
    age = Column(Integer)
    address = Column(String(20), default='深圳')
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return f"<id:{self.id},name:{self.name},age:{self.age},address:{self.address}>"


class NewWorks(Base):
    """新闻作品"""

    __tablename__ = "newWorks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    context = Column(TEXT, nullable=False)
    author = Column(String(20), nullable=False)
    length = Column(Integer)
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    # 创建一对多外键关系,表示一篇新闻有多个作者
    Author_id = Column(Integer, ForeignKey("newAuthor.id"))

    # 创建反向查找,当需要通过查询主表来对子表进行排序时添加order_by=排序字段来实现
    authorInfo = relationship("NewAuthor", backref=backref("NewWorks", order_by=length,lazy='dynamic'),
                              cascade="save-update,delete,delete-orphan", single_parent=True)

    def __repr__(self):
        return f"<id:{self.id}, context:{self.context}, length:{self.length} author:{self.author}>"


def insert():
    """创建数据"""
    with Session() as res:
        for a in range(20):
            name = "".join(i for i in random.sample(
                """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许金魏陶姜戚谢邹喻柏水窦章
                云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤""", 3))
            author = NewAuthor(name=name, gender=random.choice([False, True]),
                               age=random.randint(20, 25))
            res.add(author)

        for f in range(20):
            context = "".join(i for i in random.sample(
                """1234567890qwertyuioplkjhgfdsazxcvbnm
                QWERTYUIOPASDFGHJKLZXCVBNM""", random.randint(30, 40)))
            newWorks = NewWorks(context=context, author=name, length=len(context))
            author.NewWorks.append(newWorks)
        res.commit()


def group_by():
    """分组查询"""
    with Session() as res:
        author = res.query(NewAuthor.age, func.count(NewAuthor.id)).group_by(NewAuthor.age)
        print('返回对象:', type(author))

        author = res.query(NewAuthor.age, func.count(NewAuthor.id)).group_by(NewAuthor.age).all()
        print('年龄分组:', author)

        author = res.query(NewAuthor.age, func.count(NewAuthor.id)).group_by(NewAuthor.age).having(NewAuthor.age > 24).all()
        print('年龄分组并大于24:', author)



if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表

    # insert()

    # group_by()
    pass
