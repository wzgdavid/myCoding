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
        '''
        lines = db['chargerecord'].find({'createtime':{'$regex':'2014-03'}})
        count = 0
        for line in dblines:
            print line
            count += line['price']
        print count,'OK'       
        count = 0
        for i in range(1,32):
            str_date = '2014-03-0'+str(i)
            print str_date
            lines = db['chargerecord'].find({'createtime':{'$regex':str_date}})
            #print lines
            print lines[0]
            for line in lines:
                try:
                    count += line['price']
                except:
                    print 'bad'
        print count
        '''
        count = 0
        lines = db['chargerecord'].find({},{'price':1})
        file = open('result.txt','w')
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
        '''
        for line in lines:
            print line
            try:
                count += line['price']
            except:
                pass
            print count
        '''
    except:
        print 'bad'
if __name__ == '__main__':
    #findlist=['2100409004','2100450596']
    #mongo 54.238.211.119
    #use logawsmaxstrikedb1a
    #db.auth('logawsmaxstrikeuser1aOcdata','logawsmaxstrikeuPw2oa&oCdata')
    #host = '10.161.177.73'
    #dbname = 'logcnmaxstrikedb1a'
    #dbauth = 'logcnmaxstrikeuser1aocdata'
    #dbpasswd = 'logcnmaxstrikeuPW1oa&oCdata'
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
