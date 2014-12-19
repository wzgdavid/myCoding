#codin: utf-8
from utils import selectDB
import sys
import datetime
import json
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
uid = sys.argv[1]
if uid.startswith('1'):
    platform = "cn"
else:
    platform = "tw"
	
table_str = sys.argv[2] 
#table = selectDB.db(platform, 'log').consumerecord
#match_query = {"uid":uid,'createtime': {'$gte':"2013-12-31 00:00:00", '$lt':"2014-01-01 00:00:00"}}
##match_query = {'createtime': {'$lt':"2013-12-30 00:00:00", '$gte':"2013-12-29 13:50:00"}, "client_type":"oc_android"}
#group_query = {'_id':"$uid",'add_coin':{"$sum":"$num"}}
#
#result = table.aggregate([{"$match": match_query},{"$group":group_query}])['result']
#result.sort(key = lambda x: x['add_coin'])
#for item in result:
#   print item["_id"], item["add_coin"]

#print result

table = selectDB.db(platform, 'log')["table_str"]
find_str = json.loads(argv[3])

result = table.find(find_str)
for item in result:
   print item

