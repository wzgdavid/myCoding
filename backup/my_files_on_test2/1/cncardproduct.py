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
        lines = db['cardproduct'].find({'uid':uid,'card_msg.cid':{'$in':['267_card','198_card','263_card']}},{'_id':0})
        for line in lines:
            try:               
                print 'datetime:%s,card_msg:%s,where:%s' %(line['date_time'].strftime('%Y-%m-%d %H:%M:%S' ),line['card_msg'],line['where']),'where',line['where']
            except:
                print 'for try'
                pass
    except:
        print 'bad'
        pass
if __name__ == '__main__':
    host = '10.161.177.73'
    dbname = 'logcnmaxstrikedb1a'
    dbauth = 'logcnmaxstrikeuser1aocdata'
    dbpasswd = 'logcnmaxstrikeuPW1oa&oCdata'
    uid = raw_input('please input the uid\n')
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    print '++++++++++++++++++++++++++++++++++++++ go'
    check(db,uid)

