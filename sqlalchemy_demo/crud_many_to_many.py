from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DATETIME, TEXT
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from sqlalchemy_demo.db_tool import Base

"""
表关系存在三种, 多对多，新闻标签和新闻创建多对多关系
    
    # 默认删除策略 ondelete = 'RESTRICT'
    # 级联删除策略 ondelete = 'CASCADE'
    # 设置为空 ondelete = 'set null'
"""

# 实现原理：创建第三张表, 来关联2个模型的数据关系,必须创建在关联模型的上面

news_tag = Table(
    "t_New_Tag",
    Base.metadata,
    # 两个字段都加上primary_key=True后,会自动的组成复合组件,保证数据唯一性
    Column('new_id', Integer, ForeignKey("newWorks.id"), primary_key=True),
    Column('tag_id', Integer, ForeignKey("newTag.id"),primary_key=True),

)


class NewWorks(Base):
    """新闻作品"""

    __tablename__ = "newWorks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    context = Column(TEXT, nullable=False)
    author = Column(String(20), nullable=True)
    tags = Column(String(20))
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    # 创建反向关联,需要传入secondary=news_tag参数
    tagsInfo = relationship("NewTag", backref="NewWorks",secondary=news_tag)

    def __repr__(self):
        return f"id:{self.id}, context:{self.context}, author:{self.author},tags:{self.tags}"


class NewTag(Base):
    """新闻标签"""

    __tablename__ = "newTag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"id:{self.id}, title:{self.title}"


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表
