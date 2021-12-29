from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""
ORM介绍,对象模型与数据库表的映射
1、原生sql语句缺点,存在web安全问题,sql重复利用率不高,越复杂的sql语句,会越长越复杂,消耗高
2、ORM优点,设计灵活,易用性,可移植性,综合性能小
"""

# 数据库配置
hostname = '192.168.0.121'
port = '3306'
database = 'sqlALchemy'
username = 'mysql'
password = '123456'
db_url = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8'

# 创建数据库引擎
engine = create_engine(db_url)

# 创建链接
conn = engine.connect()
# 测试是否连接成功
result = conn.execute('select 1')

# 创建表模型
Base = declarative_base(engine)

# 获取对话对象,绑定数据库引擎
sessionObj = sessionmaker(engine)()
# print(sessionObj)

if __name__ == "__main__":
    print(result)
    print(result.fetchone())
