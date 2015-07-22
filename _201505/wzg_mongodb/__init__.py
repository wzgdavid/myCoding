# encoding: utf-8
import pymongo
'''
mongodb中一个 document 对应 python 的一个 Model 的实例的字段
一个 collection 对应一个 Model 的类
mongodb 版本 mongodb-osx-x86_64-2.6.4
'''

client = pymongo.MongoClient('localhost', 27017)

#print client

db = client.test_database # or db = client['test-database']

collection = db.test_collection # or collection = db['test-collection']

#print collection

person = {
    'pk': 'mongomodel111',
    'name': 'xsss',
    'age': 300,
}
#
#collection.insert(person)
result = collection.find({'pk': 'person555'})
#print result.batch_size
for n in result:
    print n
#print post_id


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

mongo_app = MongoApp('localhost', 27017, 'test_database', 'test_collection')


class MongoModel(object):
    #def __init__(self):
    #    self.app = mongo_app
    #    pass

    @classmethod
    def get(cls, pk):
        '''
        根据 pk 取得字段,然后生成对应的类返回
        '''
        fields = mongo_app.get(cls._pk(pk))
        if not fields:
            return None
        if fields.get('_id'):
            del fields['_id']
        print fields
        obj = cls()
        for k, v in fields.items():
            obj.__setattr__(k, v)

        return obj

    def save(self):
        print 'here in  ----------  model save'
        fields = self.__class__.fields
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
            print 'no record so save fields:', data
            mongo_app.set(data)
        # 有记录 update
        else:
            for field in fields:
                if field == 'pk':
                    pass
                else:
                    data[field] = getattr(self, field)
            print 'have record so update fields:', data
            mongo_app.update(self.pk, data)
            


    @classmethod
    def _pk(cls, pk):
        #print cls.__name__.lower() + str(pk)
        return cls.__name__.lower() + str(pk)


class Person(MongoModel):
    fields = ['pk', 'name', 'age', 'other_info']
    '''
    现在考虑字段以字典形式保存比如
    '''
    field_think = {
        'pk': 'unique',
        'name': 'str',
        'course': 'list fk',
    }
    @classmethod
    def get(cls, pk):
        obj = super(Person, cls).get(pk)
        print 'has obj? in person',obj
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
        person.name = 'init name'
        person.age = 0
        person.other_info = {
            'address': 'init address',
            'country': 'init country',
        }
        person.save()
        return person

    def grow_up(self):
        self.age += 1
        self.save()

if __name__ == '__main__':
    pass
    m = Person.get(169)
    print m.name, m.age
    m.grow_up()
    print m.age
    #m.grow_up()
    #m.save()
    #print mongo_app
    #print mongo_app.get(125556)
    #mongo_app.set(person)
    #print mongo_app.get(222)
