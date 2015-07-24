# encoding: utf-8
from config import *
import pymongo
'''
mongodb中一个 document 对应 python 的一个 Model 的实例的字段
一个 collection 对应一个 Model 的类

'''

#client = pymongo.MongoClient('localhost', 27017)
#
##print client
#
#db = client.test # or db = client['test-database']
#
#collection = db.test # or collection = db['test-collection']
#
##print collection
#
#person = {
#    'pk': 'mongomodel111',
#    'name': 'xsss',
#    'age': 300,
#}
##
#collection.insert(person)
#result = collection.find({'pk': 'person555'})



class MongoApp(object):
    def __init__(self, url, port, db, collection):
        client = pymongo.MongoClient(url, port)
        self.collection = client[db][collection]
    
    def get(self, pk):
        result = self.collection.find({'pk': pk})
        #print re
        for document in result:
            return document
        
    def set(self, value):
        self.collection.insert(value)

    def update(self, pk, value):
        #db.Account.update({"UserName":"libing"},{"$set":{"Email":"libing@126.com","Password":"123"}})
        self.collection.update({'pk': pk}, {"$set": value})

mongo_app = MongoApp(HOST, PORT, 'test', 'test')


class MongoModel(object):

    @classmethod
    def get_mongo(cls):
        return MongoApp(HOST, PORT, cls.db, cls.collection)

    @classmethod
    def get(cls, pk):
        '''
        根据 pk 取得字段,然后生成对应的类返回
        '''
        print(cls.__name__, 'asdfs')
        #mongo_app = MongoApp(HOST, PORT, cls.db, cls.collection)
        mongo_app = cls.get_mongo()
        fields = mongo_app.get(cls._pk(pk))
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
        '''
        2015-07-24
        问题：首次新插入一个person记录时（原来没记录），
        接连执行两个save比如执行grow_up()和change_name()有几个save就会存几条新记录，
        设想改进save方法，用类似原子操作或者缓存 或者其他
        '''
        print('MongoModel save()')
        fields = self.__class__.fields
        mongo_app = self.__class__.get_mongo()
        record = mongo_app.get(self.pk)
        #print 'record:', record
        
        data = {}
        # 无记录 insert
        if not record:
            #print 'save fields:', fields
            
            for field in fields:
                if field == 'pk':
                    data['pk'] = self.__class__.__name__.lower() + str(getattr(self, field))
                else:
                    data[field] = getattr(self, field)
            print('no record so save fields:', data)
            mongo_app.set(data)
        # 有记录 update
        else:
            for field in fields:
                if field == 'pk':
                    pass
                else:
                    data[field] = getattr(self, field)
            print('have record so update fields:', data)
            mongo_app.update(self.pk, data)
            

    @classmethod
    def _pk(cls, pk):
        return cls.__name__.lower() + str(pk)


class Person(MongoModel):
    db='test'
    collection='person'
    fields = ['pk', 'name', 'age', 'other_info']
    #'''
    #现在考虑字段以字典形式保存比如
    #'''
    #field_think = {
    #    'pid': 'pk',
    #    'age': 'int',
    #    'name': 'str',
    #    'course': 'list fk',
    #}
    @classmethod
    def get(cls, pk):
        obj = super(Person, cls).get(pk)
        #print('has obj? in person',obj)
        if not obj:
            obj = cls._create(pk)
            
        return obj

    @classmethod
    def _create(cls, pk):
        '''
        db 中没有对应记录,则创建一个
        '''
        person = cls()
        person.pk = pk
        person.name = ''
        person.age = 0
        person.other_info = {
            'address': '',
            'country': '',
        }
        person.save()
        return person

    def grow_up(self):
        self.age += 1
        self.save()

    def change_name(self, name):
        self.name = name
        self.save()

if __name__ == '__main__':
    pass
    m = Person.get(175)
    print(m.name, m.age)

    '''
    2015-07-24
    问题：首次新插入一个person记录时（原来没记录），
    接连执行两个save比如执行grow_up()和change_name()有几个save就会存几条新记录，
    设想改进save方法，用类似原子操作或者缓存 或者其他
    '''
    m.grow_up()
    m.change_name('jjj')
    #print(m.age)
    #m.grow_up()
    #m.save()
    #print mongo_app
    #print mongo_app.get(125556)
    #mongo_app.set(person)
    #print mongo_app.get(222)
