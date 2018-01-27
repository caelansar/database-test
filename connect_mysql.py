#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 11:44
# @Author  : caelansar
# @Site    : 
# @File    : connect_mysql.py
# @Software: PyCharm

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)

    def __repr__(self):
        return '<test %s>' %self.name

engine = create_engine('mysql+pymysql://root:password@localhost:3306/aaa')
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    t1 = Test(name='cae', age=20)
    t2 = Test(name='lan', age=20)
    session.add(t1)
    session.add(t2)
    session.commit()
    allresult = session.query(Test).filter_by(age=20).all()
    print(allresult)
    '''
    output:
    [<test cae>, <test lan>]
    '''