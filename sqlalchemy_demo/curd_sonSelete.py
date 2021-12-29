import random
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DATETIME, TEXT
from sqlalchemy import func
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from sqlalchemy_demo.db_tool import Base, engine

"""
实现数据的关联查询之子查询  .subquery()和c关键字的引用
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
    authorInfo = relationship("NewAuthor", backref=backref("NewWorks", order_by=length, lazy='dynamic'),
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

        # for f in range(10):
        #         #     context = "".join(i for i in random.sample(
        #         #         """1234567890qwertyuioplkjhgfdsazxcvbnm
        #         #         QWERTYUIOPASDFGHJKLZXCVBNM""", random.randint(30, 40)))
        #         #     newWorks = NewWorks(context=context, author=name, length=len(context),
        #         #                         Author_id=random.choice([1, 2, 3]))
        #         #     res.add(newWorks)
        res.commit()


def select():
    with Session() as res:
        """不用子查询分两次执行了sql"""
        a = res.query(NewAuthor).filter(NewAuthor.age >= 24).first()
        data = res.query(NewAuthor).filter(NewAuthor.age >= a.age).all()
        print(data)

        """利用了子查询,只执行一次sql"""
        a = res.query(NewAuthor.age.label('nage')).filter(NewAuthor.age > 24).limit(1).subquery()
        print('只获取出名字', type(a), a.c.nage)
        data = res.query(NewAuthor).filter(NewAuthor.age >= a.c.nage)
        print(data)


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表

    # insert()

    # select()
    pass
