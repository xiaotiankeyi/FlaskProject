from sqlalchemy_demo.create_tableModel import Person
from sqlalchemy_demo.db_tool import sessionObj

"""
1、创建会话对象
crud操作:
    增删改查数据
"""


def insert():
    # 添加数据
    p = Person(name='张飞', gender=True, age=34, address='荆州',
               number=123, course='java')

    p2 = Person(name='关羽', gender=False, age=21, address='四川',
               number=123, course='python')
    # 插入数据
    sessionObj.add(p)
    # 插入多条
    # sessionObj.add([p, p2])
    # 提交添加
    sessionObj.commit()


def select():
    # 查看全表时不添加all()显示原生sql语句
    sql = sessionObj.query(Person)
    # print(sql)

    # 查询所有数据
    result = sessionObj.query(Person).all()
    for result in result:
        # print(result)
        pass

    # 条件查询之filter_by
    result1 = sessionObj.query(Person).filter_by(name='jack').all()
    # print(result1)

    # 条件查询之filter
    result2 = sessionObj.query(Person).filter(Person.name == 'jack').all()
    # print(result2)

    # 条件查询之get依据id查询,不存在不会报错
    result3 = sessionObj.query(Person).get(2)
    # print(result3)

    # 条件查询之first()查询第一条
    result4 = sessionObj.query(Person).first()
    print(result4)


def update():
    """修改数据"""
    result4 = sessionObj.query(Person).first()
    # 修改name字段值
    result4.name = 'Lucy'
    # 提交修改
    sessionObj.commit()


def delete():
    result4 = sessionObj.query(Person).first()
    # 删除查询出的记录
    sessionObj.delete(result4)
    # 提交删除
    sessionObj.commit()


if __name__ == "__main__":
    insert()
    # update()
    # select()

    pass
