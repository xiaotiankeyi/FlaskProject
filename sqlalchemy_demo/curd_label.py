from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import String, Integer, DATETIME
from sqlalchemy.orm import aliased
from sqlalchemy.orm import sessionmaker

from sqlalchemy_demo.db_tool import Base, engine

"""
实现数据的关联查询之自关联查询,表名的改变
"""

Session = sessionmaker(engine)


class City(Base):
    """新闻作者表"""
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(20))
    a_id = Column(Integer)
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return f"<id:{self.id},address:{self.address}>"


def insert():
    """创建数据"""
    with Session() as res:
        cityData = City(address='江西', a_id=0)
        res.add(cityData)

        addressList = ['赣州', '鹰潭', '萍乡', '上饶', '景德镇', '新余', '吉安']
        for a in addressList:
            cityData = City(address=a, a_id=1)
            res.add(cityData)
        res.commit()


def select():
    """表名命名为a"""
    a = aliased(City)

    with Session() as res:
        val = res.query(City.id, City.address, a.address, a.id, a.a_id).join(a, City.id == a.a_id).all()
        for i in val:
            print(i)


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表

    # insert()

    # select()
    pass
