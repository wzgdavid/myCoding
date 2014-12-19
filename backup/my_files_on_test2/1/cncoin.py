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
    try:
        count = 0
        lines = db['chargerecord'].find({},{'price':1})
        file = open('cnresult.txt','w')
        for line in lines:
            try:
                count += line['price']
                file.write(line)
                file.write('\n')
                file.flush()
            except:
                pass
        file.close()
        print count,'count'
    except:
        print 'bad'
if __name__ == '__main__':
    #findlist=['2100409004','2100450596']
    #mongo 54.238.211.119
    #use logawsmaxstrikedb1a
    #db.auth('logawsmaxstrikeuser1aOcdata','logawsmaxstrikeuPw2oa&oCdata')
    host = '10.161.177.73'
    dbname = 'logcnmaxstrikedb1a'
    dbauth = 'logcnmaxstrikeuser1aocdata'
    dbpasswd = 'logcnmaxstrikeuPW1oa&oCdata'
    
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    print '++++++++++++++++++++++++++++++++++++++ go'
    check(db)
