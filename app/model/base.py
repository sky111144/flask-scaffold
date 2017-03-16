#!/usr/bin/python
#coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 创建数据库
engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/ink?charset=utf8", max_overflow = 5)

# 生成一个SqlORM 基类
Base = declarative_base()

class User(Base):
    '''
    @ 表结构：小编基本信息
    '''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(300))
    password = Column(String(100))

# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
Base.metadata.create_all(engine)

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = sessionmaker(bind=engine)
