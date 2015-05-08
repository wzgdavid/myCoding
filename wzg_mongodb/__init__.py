# encoding: utf-8
import pymongo


client = pymongo.MongoClient('localhost', 27017)

#print client

db = client.test_database # or db = client['test-database']

collection = db.test_collection # or collection = db['test-collection']

print collection

post = {
    'a': 1,
    'b': '2',
}
posts = db.posts
print posts
post_id = posts.insert_one(post)

print post_id