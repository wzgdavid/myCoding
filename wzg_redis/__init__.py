# encoding: utf-8
'''
 python与 redis 的 ORM 映射
一个 model 的字段对应 redis 里的一个字符串, 字符串是 json 格式

redis 版本 : redis-2.8.13
'''

import redis
import json

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


#person = {
#    'pk': 2,
#    'name': 'aaa',
#    'age': 66,
#}
#
#person = json.dumps(person)
#r.set('person1', person)
#pipe = r.pipeline()
#pipe.set('foo', 'pipe')
#print pipe.get('foo')
#pipe.execute()
#print r.get('foo')

#print r.exists('foo')


class Redis(object):
    def __init__(self):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.r = redis.Redis(connection_pool=pool)

    def get(self, pk):
        return self.r.get(pk)

    def set(self, pk, value):
        self.r.set(pk, value)


redis_app = Redis()


class Model(object):
    @classmethod
    def get(cls, pk):
        all_info = redis_app.get(cls.__name__.lower() + str(pk))
        #obj = type.__new__(cls, )
        if not all_info:
            return None
        obj = cls()

        all_info = json.loads(all_info)
        for k, v in all_info.items():
            obj.__setattr__(k, v)
        
        return obj

    def test(self):
        print 'model test'
        #if self.r.exists(self.__whole_pk(self.pk)):
        #    return
        #self.r.set(self.__whole_pk(self.pk))

    def save(self):
        fields = self.__class__.fields
        data = {}
        for key in fields:
            data[key] = getattr(self, key)

        #print data
        json_data = json.dumps(data)

        print 'json_data:', json_data
        redis_app.set(self.__whole_pk(self.pk), json_data)

    def delete(self, pk):
        pass

    def __whole_pk(self, pk):
        return self.__class__.__name__.lower() + str(pk)


class Person(Model):

    fields = ['pk', 'name', 'age', 'info']

    def __init__(self):
        super(Person, self).__init__()

    @classmethod
    def get(cls, pk):
        obj = super(Person, cls).get(pk)
        #print obj ,'has obj or not'
        if not obj:
            #print 'create obj'
            obj = cls.create(pk)
        return obj

    @classmethod
    def create(cls, pk):
        p = cls()
        p.pk = pk
        p.name = 'init'
        p.age = 0
        p.info = {
            'a': 1,
            'b': 2,
            'c': 'cccc',
        }
        p.save()
        return p

    def change_name(self, name):
        self.name = name
        self.save()


if __name__ == '__main__':
    # test redis
    #redis_app.set('model1', 'test model 1')
    #print redis_app.get('model1')

    #m = Model.get(1)
    #print m.test()

    p = Person.get(5591)
    print p.name
    #p.change_name('changed name2')
    #print p.name
    #print p.info['a']
    #p.change_name('cccccc')
