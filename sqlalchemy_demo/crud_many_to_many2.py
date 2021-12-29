from sqlalchemy_demo.crud_many_to_many import NewWorks, NewTag
from sqlalchemy_demo.db_tool import engine
from sqlalchemy.orm import sessionmaker

"""
多表操作之多对多操作
"""

Session = sessionmaker(engine)

def insert():
    new1 = NewWorks(context="辽宁号航母出海演习", tags="军事,热点")
    new2 = NewWorks(context="样式采访张同学", tags="娱乐")
    new3 = NewWorks(context="中共中央十六届六中全会开幕", tags="热点")

    tag1 = NewTag(title='军事')
    tag2 = NewTag(title='娱乐')
    tag3 = NewTag(title='热点')

    # 为新闻添加标签
    new1.tagsInfo.append(tag1)
    new1.tagsInfo.append(tag3)
    new2.tagsInfo.append(tag2)
    new3.tagsInfo.append(tag3)

    # 添加记录时只需要添加新闻即可
    with Session() as res:
        res.add(new1)
        res.add(new2)
        res.add(new3)

        res.commit()

def find():
    with Session() as res:
        # val = res.query(NewWorks).filter(NewWorks.id==1).all()
        # val = res.query(NewWorks).filter_by(id=1).first()
        val = res.query(NewWorks).first()

        print('新闻:', val)
        print('该新闻标签:',val.tagsInfo)

        val = res.query(NewTag).filter_by(id=2).first()
        print('标签:', val)
        print('该标签所属新闻:',val.NewWorks)
    pass

def delete():
    with Session() as res:
        val = res.query(NewWorks).filter_by(id=1).first()
        res.delete(val)
        res.commit()

if __name__ == "__main__":
    insert()
    find()
    # delete()
    pass
