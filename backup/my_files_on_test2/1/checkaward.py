#! -*- coding:utf-8 -*-
import pymongo
import json
import sys
import random
import os
import datetime
import time
import traceback
import copy
from bson.json_util import dumps
def check(db):
    '''db.chargerecord.find({'createtime':{'$gte':'2014-04-07','$lt':'2014-04-09'}}).count()'''
    lines = db['chargerecord'].find({'createtime':{'$gte':'2014-04-07','$lt':'2014-04-09'}},{'_id':0})
    countline = db['chargerecord'].find({'createtime':{'$gte':'2014-04-07','$lt':'2014-04-09'}}).count()
    count = 0
    uids = []
    allcharge = {}
    file = open('chargeresult.txt','w')
    for i in range(countline):
        line = lines[i]
        uid = line['uid']
        uids.append(uid)
        this_charge = line['after_coin'] - line['before_coin']
        try:
            allcharge[uid] += this_charge
        except:
            allcharge[uid] = this_charge
        file.write(json.dumps(line))
        file.write('\n')
        file.flush()
    file.close()
    print uids,'\n'
    uid_2310 = {}
    uid_1150 = {}
    for charge in allcharge:
        if allcharge[charge]>=2310:
            uid_2310[charge] = allcharge[charge]
        elif allcharge[charge]>=1150:
            uid_1150[charge] = allcharge[charge]
    print uid_1150
    print uid_2310
    #for line in lines:
    #    print line
        #count += line['price']
    #print count
if __name__ == '__main__':
    #findlist=['2100409004','2100450596']
    #mongo 54.238.211.119
    #use logawsmaxstrikedb1a
    #db.auth('logawsmaxstrikeuser1aOcdata','logawsmaxstrikeuPw2oa&oCdata')

    dbname = 'logawsmaxstrikedb1a'
    dbauth = 'logawsmaxstrikeuser1aOcdata'
    dbpasswd = 'logawsmaxstrikeuPw2oa&oCdata'
    host = '54.238.211.119'
    
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    #tablegacha = 'cardproduct'
    #tablesoul = 'soulproduct'
    print '++++++++++++++++++++++++++++++++++++++ go'
    check(db)
