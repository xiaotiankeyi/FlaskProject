"""
limit指定获取几条数据
offset跳过几条数据
slice切片指定【头，尾】
分页操作
"""
from sqlalchemy.orm import sessionmaker

from sqlalchemy_demo.curd_order_by import NewAuthor
from sqlalchemy_demo.db_tool import engine
from sqlalchemy import func

Session = sessionmaker(engine)


def select_limit():
    with Session() as res:
        # 指定获取几条limit
        val = res.query(NewAuthor).limit(3).all()
        print(val)

        # 排除几条offset
        val = res.query(NewAuthor).offset(3).all()
        print(val)


        # 分页方式一
        # count = res.query(func.count(NewAuthor.id)).first()
        # print(count[0])
        val = res.query(NewAuthor).limit(3).offset(3).all()
        print(val)

        # 分页方式二
        val = res.query(NewAuthor).slice(6, 9).all()
        print(val)

if __name__ == "__main__":
    select_limit()
