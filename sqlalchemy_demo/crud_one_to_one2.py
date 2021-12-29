from sqlalchemy_demo.crud_one_to_one import NewAuthor, NewAuthorInfo, \
    NewPress
from sqlalchemy_demo.db_tool import sessionObj

"""
多表操作
"""


def insert():
    """添加出版社在添加作者后关联出版社"""
    press = NewPress(pressName='清华出版社', address='北京')  # 出版社
    sessionObj.add(press)
    sessionObj.commit()

    # 从authorInfo表方面加
    authorInfo = NewAuthorInfo(gender=False, age=25, address='南京', press_id=1)  # 用户信息
    author = NewAuthor(name='jack')  # 作者
    authorInfo.newAuthor = author  # 一对一关系需要创建关联后,authorInfo记录会同步添加,涉及到级联操作
    sessionObj.add(authorInfo)
    sessionObj.commit()

    # 从author表方面加
    author = NewAuthor(name='Tom')  # 作者
    authorInfo = NewAuthorInfo(gender=True, age=20, address='天津', press_id=1)  # 用户信息
    author.newAuthorInfo = authorInfo  # 一对一关系需要创建关联后,authorInfo记录会同步添加
    sessionObj.add(author)
    sessionObj.commit()


def find():
    """通过用户信息表反向查找出作者名称和所在出版社"""
    info = sessionObj.query(NewAuthorInfo).first()
    print('1、作者信息:', info)
    print('2、作者：', info.newAuthor)
    print('3、该作者所处出版社:', info.pressData)

    print("*" * 60)

    """通过查找作者名字表反向查找出作者详细信息"""
    info = sessionObj.query(NewAuthor).first()
    print('4、作者:', info)
    print('5、作者信息:', info.newAuthorInfo)

    print("*" * 60)

    info = sessionObj.query(NewPress).first()
    print('6、出版社:', info)
    print("7、该出版社人员:", info.NewAuthorInfo)


if __name__ == "__main__":
    # insert()
    # find()
    pass
