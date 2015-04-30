# encoding: utf-8
import pymongo

conn = pymongo.Connection('localhost', 27017)

db = conn.temp

students = db.students

#students.insert({'name': 'abc','pk': 123})

result = students.find({'name': 'bbb'})

#for n in result:
#    print n


class MongeDB(object):
    def __init__(self):
        conn = pymongo.Connection('localhost',27017)
        self.db = conn.temp

    def get(self, pk):
        '''
        从 document 中取得 pk的记录
        '''
        #result = self.db[obj.__class__.__name__].find({'pk':pk})
        result = self.db[self.__class__.__name__.lower()].find({'pk': pk})
        return result

    def save(self, pk):
        '''
        保存 pk 这条记录
        '''
        self.db[self.__class__.__name__.lower()].update({'pk': pk}, )

class Students(MongeDB):
    """
    pk定义主键
    fields定义需要持久化的字段
    """
    fields = ['name', 'age']
    pass


s = Students()

r = s.get(123)
for n in r:
    print n
