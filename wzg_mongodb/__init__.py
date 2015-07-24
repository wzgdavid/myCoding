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
    class Employee(EasyModel):
        db='test'
        collection='employee'
        fields = ['pk', 'name', 'salary', 'other_info']
    
        @classmethod
        def _init_instance(cls, pk):
            employee = cls()
            employee.pk = pk
            employee.name = ''
            employee.salary = 0
            employee.other_info = {
                'phone_number': '',
                'address': '',
            }
            employee.save()
            return employee
    
        def raise_salary(self, amount):
            self.salary += amount
            self.save()


    class Company(EasyModel):
        db='test'
        collection='company'
        fields = ['pk', 'name', 'staff']

        @classmethod
        def _init_instance(cls, pk):
            company = cls()
            company.pk = pk
            company.name = ''
            company.staff = []
            company.save()
            return company

        def add_employee(self, employee):
            self.staff.append(employee)
            self.save()

    '''
    问题： 怎么实现这样的效果
    '''
    employee1 = Employee.get(2)
    company = Company.get(1)
    company.add_employee(employee1) # 然后company的文档中多了一个employee的pk

