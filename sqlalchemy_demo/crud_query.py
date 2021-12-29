from sqlalchemy import func

from sqlalchemy_demo.create_tableModel import Person
from sqlalchemy_demo.db_tool import sessionObj

"""
query查询函数的使用及可专递参数
    1、模型名(对应为所有查询)
    2、模型中的属性
    3、聚合函数

"""

all = sessionObj.query(Person).all()  # 模型名=全表查询
print(all)

single = sessionObj.query(Person).filter_by(age=23).all()  # 某属性查询
# print(single)

# 聚合函数查询
sql = sessionObj.query(func.count(Person.id))  # 只查看原生sql语句
count = sessionObj.query(func.count(Person.id)).first()
max = sessionObj.query(func.max(Person.age)).first()
min = sessionObj.query(func.min(Person.age)).first()
avg = sessionObj.query(func.avg(Person.age)).first()
sum = sessionObj.query(func.sum(Person.age)).first()

# print(sum)

if __name__ == "__main__":
    pass
