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
    findlist = ['2100523071']
    for find in findlist:
        try:
            prolines = db['soulproduct'].find({'uid':find})[:5]
            '''
            dblines = copy.deepcopy(prolines)
            prlines = copy.deepcopy(dblines)
            l1 = []
            l2 = []
            i = 0
            for line in prlines:
                print 1
                l1.append(line)
            for ll in dblines:
                l2.append(ll)
                print 2
            for oo in l1:
                for pp in l2:
                    print 3
            '''
            start = time.time()
            #for line in json.loads(dumps(prolines)):
            #   print line
            jslines = json.loads(dumps(prolines))
            print type(jslines)

            end = time.time()
            print end - start
            start = time.time()
            li = []
            for line in prolines:
                li.append(line)
            print type(li)
            end = time.time()
            print end-start  
        except:
            print 'this is bad line'



if __name__ == '__main__':
    #findlist=['2100409004','2100450596']

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
