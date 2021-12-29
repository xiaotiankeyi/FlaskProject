"""
lazy=`dynamic`懒加载应用
注意:只可以引用在一对多或是多对多关系中
    authorInfo = relationship("NewAuthor",
            backref=backref("NewWorks", order_by=length,lazy='dynamic'),
                cascade="save-update,delete,delete-orphan", single_parent=True)
"""

from sqlalchemy.orm import sessionmaker

from sqlalchemy_demo.curd_order_by import NewAuthor, NewWorks
from sqlalchemy_demo.db_tool import engine

Session = sessionmaker(engine)


def select():
    with Session() as res:
        val = res.query(NewAuthor).all()

        print(type(val[-1].NewWorks))

        # 对用户查找出来的文章进行过滤
        val = val[-1].NewWorks.filter(NewWorks.length > 15).all()
        print(val)


if __name__ == "__main__":
    select()
