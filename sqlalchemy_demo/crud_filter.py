from sqlalchemy import and_
from sqlalchemy import or_

from sqlalchemy_demo.create_tableModel import Person
from sqlalchemy_demo.db_tool import sessionObj

"""
filter方法常用的过滤条件,下面介绍的方法只能有filter调用实现
"""

# 等值查询 equal    ==
# 非等值查询 equal   !=
# 模糊查询  like("%a%")
# 模糊查询之不区分大小写  ilike("%a%")
# 多值查询  in_(['a', 'b', 'c'])
# not in   ~模型.属性.in_(['a', 'f','g'])
# is null   ==None
# is null   is_(None)
# is not null   !=None
# is not null   isnot(None)
# and   filter(_and(条件一,条件二))
# and   filter(条件一,条件二)
# or    filter(or_(条件一,条件二))

equal = sessionObj.query(Person).filter(Person.name == 'jack').first()
print(equal)

equal = sessionObj.query(Person).filter(Person.name != 'jack').all()
print(equal)

equal = sessionObj.query(Person).filter(Person.name.like('%志%')).all()
print(equal)

equal = sessionObj.query(Person).filter(Person.name.in_(['jack', 'Tom'])).all()
print(equal)

equal = sessionObj.query(Person).filter(~Person.name.in_(['jack', 'Tom'])).all()
print(equal)

equal = sessionObj.query(Person).filter(Person.age == None).all()
print('为空', equal)
equal = sessionObj.query(Person).filter(Person.age.is_(None)).all()
print('为空', equal)
equal = sessionObj.query(Person).filter(Person.age != None).all()
print('不为空', equal)
equal = sessionObj.query(Person).filter(Person.age.isnot(None)).all()
print('不为空', equal)

equal = sessionObj.query(Person).filter(Person.age != None, Person.gender == False).all()
print('and', equal)
equal = sessionObj.query(Person).filter(and_(Person.age != None, Person.gender == False)).all()
print('and', equal)

equal = sessionObj.query(Person).filter(or_(Person.age != None, Person.gender == True)).all()
print('or', equal)

if __name__ == "__main__":
    pass
