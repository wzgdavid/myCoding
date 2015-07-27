# encoding: utf-8
import sys
sys.path.insert(0, 'C:\\Users\\Administrator\\Desktop\\myCoding')

from wzg_mongodb.config import *
import pymongo
import collections
'''
mongodb中一个 document 对应 python 的一个 Model 的实例的字段
一个 collection 对应一个 Model 的类
'''

class MongoApp(object):
    '''这个类操作pymongo'''
    def __init__(self, url, port, db, collection):
        client = pymongo.MongoClient(url, port)
        self.collection = client[db][collection]
    
    def get(self, pk):
        result = self.collection.find_one({'pk': pk})
        return result
        
    def set(self, value):
        self.collection.insert(value)

    def update(self, pk, value):
        self.collection.update({'pk': pk}, {"$set": value})

    def upsert(self, pk, value):
        self.collection.update({'pk': pk}, {"$set": value}, True)

    def get_embdoc_in_array(self, pk, info):
        '''
        得到内嵌array中的文档
        info 结构
        {
            'field_d': 内嵌文档要查找的字段
            'value': 对应的值
            'field': 文档的字段（此字段下是内嵌的array型文档）
        }
        '''
        f = info['field']
        d = info['field_d']
        v = info['value']
        fd = f + '.' + d
        #print(k,v)
        result = self.collection.find_one({fd: v}, {f: 1, '_id': 0}) 
        print(result)
        for n in result[f]:
            if n[d] == v:
                return n
        return None


class MongoModel(object):
    '''
    这个类操作MongoApp
    '''
    @classmethod
    def get_mongoapp(cls):
        collection = cls.collection.split('.')[0]
        return MongoApp(HOST, PORT, cls.db, collection)

    @classmethod
    def get(cls, pk):
        '''
        根据 pk 取得字段,然后生成对应的类返回
        '''
        mongo_app = cls.get_mongoapp()
        fields = mongo_app.get(pk)
        if not fields:
            return None
        if fields.get('_id'):
            del fields['_id']
        #print(fields)
        obj = cls()
        for k, v in fields.items():
            obj.__setattr__(k, v)

        return obj


    def save(self):
        data = {}
        fields = self.__class__.fields
        mongo_app = self.__class__.get_mongoapp()

        for field in fields:
            data[field] = getattr(self, field)
        mongo_app.upsert(self.pk, data)

    @classmethod
    def _pk(cls, pk):
        #return cls.__name__.lower() + str(pk)
        return str(pk)

'''这一层的model脱离mongo的操作'''
class EasyModel(MongoModel):
    ''''''
    @classmethod
    def get(cls, pk):
        obj = super(EasyModel, cls).get(pk)
        if not obj:
            obj = cls._init_instance(pk)
        # print(cls.__name__,'class name')
        return obj


class EmbeddedModel(MongoModel):
    '''表示内嵌的文档'''
    @classmethod
    def get(cls, pk):
        obj = super(EasyModel, cls).get(pk)
        if not obj:
            obj = cls._init_instance(pk)
        # print(cls.__name__,'class name')
        return obj


class Array(collections.Sequence):

    def add(self, item):
        pass