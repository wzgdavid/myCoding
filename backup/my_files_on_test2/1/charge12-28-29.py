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

#import pdb; pdb.set_trace()
table = selectDB.db('cn', 'log').chargerecord
print table.find_one()
match_query = {'createtime': {'$gte':"2014-02-14 00:00:00", '$lt':"2014-02-15 00:00:00"},"charge_way":""}
#match_query = {'createtime': {'$lt':"2013-12-30 00:00:00", '$gte':"2013-12-29 13:50:00"}, "client_type":"oc_android"}
#group_query = {'_id':"$uid",'add_coin':{"$sum":{"$subtract":["$after_coin", "$before_coin"]}}}
group_query = {'_id':"$uid",'charge':{"$sum": "$price"}}

result = table.aggregate([{"$match": match_query},{"$group":group_query}])['result']
result.sort(key = lambda x: x['charge'])
for item in result:
   print item["_id"], item["charge"]

print result
