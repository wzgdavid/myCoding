# encoding: utf-8
from config import *
import pymongo
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


class MongoModel(object):
    '''
    这个类操作MongoApp
    '''
    @classmethod
    def get_mongoapp(cls):
        return MongoApp(HOST, PORT, cls.db, cls.collection)

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


class EasyModel(MongoModel):
    '''这一层脱离mongo的操作'''
    @classmethod
    def get(cls, pk):
        obj = super(EasyModel, cls).get(pk)
        if not obj:
            obj = cls._init_instance(pk)
        # print(cls.__name__,'class name')
        return obj


if __name__ == '__main__':
    class Person(EasyModel):
        '''具体的应用示例'''
    
        db='test'
        collection='person'
        fields = ['pk', 'name', 'age', 'other_info']
    
        @classmethod
        def _init_instance(cls, pk):
            person = cls()
            person.pk = pk
            person.name = ''
            person.age = 0
            person.other_info = {
                'phone_number': '',
                'address': '',
            }
            person.save()
            return person
    
        def grow_up(self):
            self.age += 1
            self.save()
    
        def change_name(self, name):
            self.name = name
            self.save()


    m = Person.get(2)
    print(m.name, m.age)
    m.grow_up()
    m.change_name('yy')

