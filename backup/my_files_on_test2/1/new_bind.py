#codin: utf-8
from utils import selectDB
import datetime
"""
    LOG_TABLES

buildupdate
cardconsume
carddeck
cardproduct
cardupdate
cardupgrade
chargerecord
chargeresultlog
coinconsume
coinproduct
consumerecord
dungeonrecord
equconsume
equproduct
feed
goldconsume
goldproduct
invite
itemconsume
itemproduct
loginrecord
matconsume
matproduct
newguide
pvprecord
stoneconsume
stoneproduct
system.indexes
system.users
userlevelhistory
"""

platform = "cn"

#import pdb; pdb.set_trace()
db = selectDB.db(platform, 'log')
table = db.newguide
#match_query = {'createtime': {'$gte':"2013-12-28 00:00:00", '$lte':"2013-12-29 13:50:00"}, "client_type":"oc_android"}
##match_query = {'createtime': {'$lt':"2013-12-30 00:00:00", '$gte':"2013-12-29 13:50:00"}, "client_type":"oc_android"}
#group_query = {'_id':"$uid",'add_coin':{"$sum":{"$subtract":["$after_coin", "$before_coin"]}}}
print table
print table.find_one()
result = table.find({"step":10, "date_time":{"$gte":datetime.datetime(2013,12,19),"$lt":datetime.datetime(2013,12,26)}})

new_uids = [item['uid'] for item in result]


db = selectDB.db(platform, 'online')
table = db.userbase

result = table.find({"uid":{"$in":new_uids}, 'baseinfo.bind_time': {'$ne':None}})
print result
#result = table.find("uid":{"$in":new_uids})

#for uid in new_uids:
#    
#   print item["uid"]
#print result.count()

#print result
