from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DATETIME, TEXT
from sqlalchemy.orm import relationship

from sqlalchemy_demo.db_tool import Base

"""
表关系存在三种, 一对多，,ForeignKey的使用
一对多时关键字ForeignKey创建在多的一边
    relationships方法中cascade参数的应用
    
    观点:删除主表数据时,默认情况下子表数据修改外键字段为null
    
    =save-update    实现级联写入,
    =delete     实现主表数据删除后,子表数据相关联的数据也删除
    =delete  delete-orphan    当主表解除了和子表的关联关系后,向关联的子表数据会被清空
"""


class NewAuthor(Base):
    """新闻作者表"""
    __tablename__ = "newAuthor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    gender = Column(Boolean)
    age = Column(Integer)
    address = Column(String(20))
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    # 创建反向查找,当需要主表查找子表信息时添加backref="NewAuthor",级联操作添加 cascade='save-update'
    # newInfo = relationship("NewWorks", backref="NewAuthor",cascade="save-update,delete")
    newInfo = relationship("NewWorks", backref="NewAuthor",
                           cascade="save-update,delete,delete-orphan",single_parent=True)


    def __repr__(self):
        return f"id:{self.id},name:{self.name},age:{self.age},address:{self.address}"


class NewWorks(Base):
    """新闻作品"""

    __tablename__ = "newWorks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    context = Column(TEXT, nullable=False)
    author = Column(String(20), nullable=False)
    tags = Column(Integer)
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    # 创建一对多外键关系,表示一篇新闻有多个作者
    Author_id = Column(Integer, ForeignKey("newAuthor.id"))

    def __repr__(self):
        return f"id:{self.id}, context:{self.context}, author:{self.author}"


class NewPress(Base):
    """新闻出版社"""
    __tablename__ = "newPress"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pressName = Column(String(50), nullable=False)
    address = Column(String(10))
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    # 创建一对多外键关系,表示一个出版社有多个作者
    Author_id = Column(Integer, ForeignKey("newAuthor.id", ondelete="CASCADE"))
    # 创建反向查找
    authorInfo = relationship("NewAuthor", backref="NewPress")


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表
