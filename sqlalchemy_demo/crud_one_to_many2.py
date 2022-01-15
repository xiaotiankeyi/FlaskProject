from sqlalchemy_demo.crud_one_to_many import NewAuthor, NewWorks
from sqlalchemy_demo.db_tool import sessionObj

"""
多表操作之一对多关系操作,
"""


def insert():
    author1 = NewAuthor(name='赖志添', age=23, gender=True)
    author2 = NewAuthor(name='陈辰', age=25, gender=False)
    sessionObj.add(author2)
    sessionObj.commit()

    val = sessionObj.query(NewAuthor).first()

    works = NewWorks(context='测试一对多关系', author=val.name, Author_id=val.id)
    works = NewWorks(context='通过反向查找获取一个用户有多少篇新闻',
                     author=val.name, Author_id=val.id)

    sessionObj.add(works)
    sessionObj.commit()


def find():
    val = sessionObj.query(NewAuthor).first()
    print(val)
    print('1、通过查找作者来反向查找当前用户有所少篇新闻:', val.NewWorks)

    # val = sessionObj.query(NewWorks).first()
    val = sessionObj.query(NewWorks).filter(NewWorks.id == 1).first()

    print(val)
    print('2、通过查找新闻来反向查找出当前新闻的作者:', val.authorInfo)


def delete():
    val = sessionObj.query(NewAuthor).first()
    # 子表NewWorks中关联字段Author_id设置了不可为空,所以不可删除相关联的主表数据
    sessionObj.delete(val)
    sessionObj.commit()


if __name__ == "__main__":
    # insert()
    # find()
    # delete()
    pass
