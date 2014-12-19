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
def check(db,uid):
    try:
        count = 0
        lines = db['dungeonrecord'].find({'uid':uid})
        count = db['dungeonrecord'].find({'uid':uid})
        for i in range(count):
            try:
                print lines[i]
            except:
                pass
    except:
        print 'bad'
if __name__ == '__main__':
    dbname = 'logawsmaxstrikedb1a'
    dbauth = 'logawsmaxstrikeuser1aOcdata'
    dbpasswd = 'logawsmaxstrikeuPw2oa&oCdata'
    host = '54.238.211.119'
    uid = raw_input('please input the uid\n') 
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    print 'ready to  go'
    check(db,uid)
