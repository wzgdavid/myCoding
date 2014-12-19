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



    dbname = 'qz_stg_db'
    dbauth = 'qzstguser'
    dbpasswd = 'lB7vTBor99yYh7E3F7'
    host = 'x.x.x.x'
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    return db

def show_all_collections():
    print init().collection_names()
#show_all_collections()
'''
result of show_all_collections

[
    "system.users", 
    "system.indexes", 
    "username", 
    "config", 
    "usercards", 
    "userbase", 
    "friend", 
    "accountoneclick", 
    "userlogin", 
    "usercollection", 
    "usercity", 
    "usergacha", 
    "userproperty", 
    "userpvp", 
    "usergift", 
    "userequips", 
    "userlend", 
    "leveluser", 
    "userdungeon", 
    "ptusers", 
    "moderator", 
    "sequence", 
    "userhunt", 
    "random_names", 
    "random_code", 
    "usersouls", 
    "usermysterystore", 
    "usermarquee", 
    "accountmapping", 
    "mongoconfig", 
    "giftcode", 
    "usermail", 
    "equipsouluser", 
    "ocmoderator", 
    "role", 
    "names", 
    "updateconfrecord", 
    "userpack", 
    "useractivity", 
    "insert({u'_id':", 
    "userrealpvp", 
    "userpkstore", 
    "myresults", 
    "bulletin", 
    "rediscaptchadict"
]
'''
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

def see_cards_by_uid(uid):
    db = init()
    #return db.usercards.find().count()
    return db.usercards.find_one({'uid':uid})
print see_cards_by_uid('56100215412')
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
    #see_log('newguide')
    #see_log_by_uid('newguide','1100833829')
