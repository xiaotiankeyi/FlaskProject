from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DATETIME
from sqlalchemy.orm import relationship, backref

from sqlalchemy_demo.db_tool import Base

"""
表关系存在三种, 一对一,ForeignKey的使用
创建一对一关系时 需要在relationship中添加uselist=False参数

relationships反向查找,只写一边表就可以
    # 默认删除策略 ondelete = 'RESTRICT'
    # 级联删除策略 ondelete = 'CASCADE'
    # 设置为空 ondelete = 'set null'
"""


class NewAuthor(Base):
    """新闻作者表只记录名字"""
    __tablename__ = "newAuthor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)

    def __repr__(self):
        return f"id:{self.id}, name:{self.name}"


class NewAuthorInfo(Base):
    """新闻作者表,作者详细信息表"""
    __tablename__ = "newAuthorInfo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(Boolean)
    age = Column(Integer)
    address = Column(String(20))
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    # 创建用户新闻作者表和新闻作者信息表的一对一外键关系
    Author_id = Column(Integer, ForeignKey("newAuthor.id", ondelete="CASCADE"))
    # 创建反向查询两种方式,跟作者表是一对一关系,关键在于控制uselist=False
    # newAuthor = relationship("NewAuthor", backref="newAuthorInfo", uselist=False)
    newAuthor = relationship("NewAuthor", backref=backref("newAuthorInfo", uselist=False))

    # 跟出版社是一对多关系
    press_id = Column(Integer, ForeignKey("newPress.id", ondelete="SET NULL"))

    def __repr__(self):
        return f"id:{self.id}, gender:{self.gender}, age:{self.age}, address:{self.address}"


class NewPress(Base):
    """新闻出版社"""
    __tablename__ = "newPress"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pressName = Column(String(50), nullable=False)
    address = Column(String(10))
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"id:{self.id}, pressName:{self.pressName}, address:{self.address}"


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表
