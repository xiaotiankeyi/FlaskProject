from sqlalchemy_demo.relationship_cascade import NewAuthor, NewWorks, NewPress
from sqlalchemy_demo.db_tool import sessionObj

"""
多表操作之一对多关系操作,
"""


def insert_cascade():
    # 级联操作,添加作者时添加新闻，省去了添加新闻操作
    author2 = NewAuthor(name='陈辰', age=25, gender=False)
    works = NewWorks(context='通过反向查找获取一个用户有多少篇新闻', author='陈辰', Author_id=1)

    author2.newInfo.append(works)

    sessionObj.add(author2)
    sessionObj.commit()


    press = NewPress(pressName='新华出版社', address='北京', Author_id=1)
    sessionObj.add(press)
    sessionObj.commit()


def find():
    val = sessionObj.query(NewAuthor).first()
    print(val)
    print('1、通过查找作者来反向查找当前用户有所少篇新闻:', val.newInfo)

    # val = sessionObj.query(NewWorks).first()
    val = sessionObj.query(NewWorks).filter(NewWorks.id == 1).first()

    print(val)
    print('2、通过查找新闻来反向查找出当前新闻的作者:', val.NewAuthor)

    val = sessionObj.query(NewPress).first()
    print('出版社:', val)
    print('该出版社的人员有:', val.authorInfo)


def delete():
    val = sessionObj.query(NewAuthor).first()
    # 子表NewWorks中关联字段Author_id设置了不可为空,所以不可删除相关联的主表数据
    sessionObj.delete(val)
    sessionObj.commit()

def update():
    val = sessionObj.query(NewAuthor).first()
    val.newInfo=[]
    sessionObj.commit()


if __name__ == "__main__":
    # insert_cascade()
    # find()
    # delete()
    update()
    pass
