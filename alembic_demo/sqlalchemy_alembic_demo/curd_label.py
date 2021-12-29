from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import String, Integer, DATETIME, FLOAT
from sqlalchemy.orm import sessionmaker

from db_tool import Base, engine

"""
alembic练习应用
"""

Session = sessionmaker(engine)


class City(Base):
    """新闻作者表"""
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(20))
    a_id = Column(Integer)
    acreage = Column(Integer)
    population = Column(Integer,name='人口')
    income = Column(FLOAT, name='收入')
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return f"<id:{self.id},address:{self.address}>"


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表

    pass
