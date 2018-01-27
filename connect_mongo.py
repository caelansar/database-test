#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 10:50
# @Author  : caelansar
# @Site    : 
# @File    : connect_mongo.py
# @Software: PyCharm

from pymongo import MongoClient
class Mongo():
    uri = 'mongodb://127.0.0.1:27017'
    db = None

    @staticmethod
    def init():
        client = MongoClient(Mongo.uri)
        Mongo.db = client['testmongo']

    @staticmethod
    def insert(collection, data):
        '''
        :param collection: table name
        :param data: dict or list
        :return: None
        '''
        Mongo.db[collection].insert(data)

    @staticmethod
    def update(collection, query, data):
        Mongo.db[collection].update(query, {"$set": data})

    @staticmethod
    def delete(collection, data):
        Mongo.db[collection].remove(data)

    @staticmethod
    def find(collection, query):
        return Mongo.db[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Mongo.db[collection].find_one(query)

if __name__ == '__main__':
    Mongo.init()
    Mongo.insert('test',
                 [
                    {'name': 'lbw', 'age': 25},
                    {'name': 'pdd', 'age': 25}
                ])
    Mongo.insert('test',{'name':'cae','age':20})
    for i in Mongo.find('test',{}):
        print(i)




