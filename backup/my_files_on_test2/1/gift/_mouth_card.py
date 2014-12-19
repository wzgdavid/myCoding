#coding: utf-8
from utils import selectDB
import sys
import time
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
platform = "tw"
table_str = "usergift"
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

table = selectDB.db(platform, 'online')[table_str]
uids = [
    "2100450596",
    "2100534531",
    "2100521253",
    "2100518471",
    "2100474328",
    "2100242374",
    "2100225843",
    "2100489660",
    "2100213364",
    "2100444225",
    "2100536506",
    "2100430003",
    "2100537130",
    "2100255602",
    "2100533399",
    "2100468613",
    "2100234249",
    "2100336487",
    "2100517181",
    "2100236229",
    "2100243798",
    "2100309875",
    "2100449752",
    "2100516873",
    "2100516713",
    "2100517860",
    "2100526439",
    "2100352435",
    "2100468467",
    "2100310040",
    "2100537697",
    "2100539628",
    "2100443297",
    "2100532603",
    "2100483700",
    "2100432594",
    "2100542097",
    "2100539149",
    "2100304707",
    "2100526974",
    "2100363155",
    "2100425817",
    "2100426842",
    "2100539242",
    "2100366276",
    "2100442643",
    "2100537942",
    "2100403101",
    "2100412714",
    "2100369573",
    "2100379921",
    "2100540789",
    "2100483880",
    "2100489488",
    "2100357304",
    "2100532368",
    "2100455982",
    "2100533972",
    "2100335061",
    "2100262408",
    "2100409639",
    "2100535057",
    "2100406175",
    "2100456727",
    "2100273252",
    "2100405923",
    "2100528498",
    "2100227898",
    "2100308572",
    "2100419467",
    "2100390963",
    "2100523071",
    "2100383267",
    "2100535881",
    "2100259117",
    "2100355303",
    "2100534923",
    "2100533115",
    "2100367193",
    "2100435815",
    "2100542833",
    "2100451056",
    "2100495048",
    "2100238283",
    "2100335623",
    "2100536153",
    "2100336647",
    "2100538125",
    "2100252660"
]
for uid in uids: 
    find_str = {'uid': uid}
    gift_dict = table.find(find_str)[0]["gift_list"]
    keys = sorted(gift_dict.keys(), reverse=True) 
    for key in keys:
        if u"财源滚滚每天返还奖励:" in gift_dict[key]['content']:
            print uid, gift_dict[key]['content'],gift_dict[key]['award'], time.strftime("%Y%m%d %H:%M:%S", time.localtime(int(gift_dict[key]['upd_time']))), gift_dict[key]['has_got'] 
            break
    #else:
    #    print uid, "got coin"
