# encoding: utf-8
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
def init():
    #findlist=['2100409004','2100450596']
    #mongo 54.238.211.119
    #use logawsmaxstrikedb1a
    #db.auth('logawsmaxstrikeuser1aOcdata','logawsmaxstrikeuPw2oa&oCdata')


    dbname = 'logcnmaxstrikedb1a'
    dbauth = 'logcnmaxstrikeuser1aocdata'
    dbpasswd = 'logcnmaxstrikeuPW1oa&oCdata'
    host = '10.161.177.73'
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    return db

def see_charge_record(db):
    '''db.chargerecord.find({'createtime':{'$gte':'2014-04-07','$lt':'2014-04-09'}}).count()'''
    lines = db['chargerecord'].find({'createtime':{'$gte':'2014-04-07','$lt':'2014-04-09'}},{'_id':0})
    countline = db['chargerecord'].find({'createtime':{'$gte':'2014-04-07','$lt':'2014-04-09'}}).count()
    file = open('chargeresult.txt','w')
    for line in lines:
        uid = line['uid']
        this_charge = line['after_coin'] - line['before_coin']
        file.write(json.dumps(line))
        file.write('\n')
        file.flush()
    file.close()

    #one_record = db['chargerecord'].find_one()
    #print one_record
'''
def see_coin_consume(db):
    lines = db['coinconsume'].find({'date_time':{'$gte':datetime.datetime(2014,10,15)}},{'_id':0})
    #lines = db['coinconsume'].find()

    for line in lines:
        uid = line['uid']
        print line

    #one_record = db['chargerecord'].find_one()

    #print one_record
'''
def see_log(collection):  # by date_time
    '''
    10-15
    collection 在data_log_mod.py的ALL_LOG_NAMES 里，改成小写
    '''
    db = init()
    lines = db[collection].find({'date_time':{'$gte':datetime.datetime(2014,10,23,13)}},{'_id':0})


    #lines = db['coinconsume'].find()

    for line in lines:
        uid = line['uid']
        print line

    #one_record = db[collection].find_one()
    #print one_record

def see_log_by_uid(collection, uid):
    '''
    10-15
    collection 在data_log_mod.py的ALL_LOG_NAMES 里，改成小写
    '''
    db = init()
    lines = db[collection].find({'uid':uid},{'_id':0})

    #lines = db['coinconsume'].find()

    for line in lines:
        uid = line['uid']
        print line

if __name__ == '__main__':

    print '\n\n +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ go'
    see_log('newguide')
    #see_log_by_uid('newguide','1100833829')
