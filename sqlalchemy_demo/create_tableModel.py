import enum
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DATETIME
from sqlalchemy import Enum
from sqlalchemy import Integer, String, Boolean, DECIMAL

from sqlalchemy_demo.db_tool import Base

# 创建数据库基类
"""
常用的基本数据类型
    String  可变字符串
    Decimal     定点类型
    Enum    枚举类型   Enum("python", "java")
    Data    存储年/月/日
    DataTime    存储年月日时分秒
    Time    存储时分秒
    Text    存储6w字符
    
Column函数关键字参数
    primary_key     字段为主键
    autoincrement   设置自增
    default     默认值
    nullable    是否为空
    unique  是否唯一
    onupdate    记录数据更新时间
    name    指定表字段名
"""


class EnumTag(enum.Enum):
    """定义枚举选项"""
    python = "python"
    java = "java"
    php = "php"


class Person(Base):
    # 表名格式__tablename__
    __tablename__ = "t_user"

    # 创建数据表字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    gender = Column(Boolean)
    age = Column(Integer)
    address = Column(String(20))
    number = Column(DECIMAL(10, 4))
    # course = Column(Enum("python", "java", "php"))
    course = Column(Enum(EnumTag))
    update_time = Column(DATETIME, name='修改时间', onupdate=datetime.now)

    def __repr__(self):
        return f"id:{self.id},name:{self.name},gender:{self.gender}," \
            f"age:{self.age},address:{self.address},number:{self.number}," \
            f"course:{self.course}"


# 把创建好的模型映射到数据库中,注意,映射好后,后面在添加的字段将不会在做映射


if __name__ == "__main__":
    Base.metadata.drop_all()  # 删除表
    Base.metadata.create_all()  # 创建表
    pass
