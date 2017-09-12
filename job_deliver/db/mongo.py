# encoding:utf-8 
import json
import pymongo
def foo():
    print "foo in mongo"
    return "foo in mongo"

#db.test.create_index([('job', pymongo.ASCENDING), ('company', pymongo.ASCENDING)], unique=True)

def get_jobs():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['test']
    collection = db['test']
    results = collection.find({}, {'_id': 0}) # 不要_id字段
    result_list = []
    for n in results:
        #print n
        result_list.append(n)
    #dumped = json.dumps(result_list)
    return result_list

if __name__ == '__main__':
    
    client = pymongo.MongoClient('localhost', 27017)
    db = client['test']
    collection = db['test']

    #db.test.drop()
    results = collection.find({}, {'_id': 0}) # 不要_id字段

    result_list = []
    for n in results:
        #print n
        result_list.append(n)
    dumped = json.dumps(result_list)
    print dumped
    #db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
    #db.test.create_index([('job', pymongo.ASCENDING), ('company', pymongo.ASCENDING)], unique=True)