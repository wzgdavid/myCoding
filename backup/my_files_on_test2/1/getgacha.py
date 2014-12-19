#! -*- coding:utf-8 -*-
import pymongo
import json
import sys
import random
import os
import datetime
import time
import traceback

def check(db,tablegacha,tablesoul):
    '''
    findlist=['2100409004','2100450596']
    dbname = 'logawsmaxstrikedb1a'
    dbauth = 'logawsmaxstrikeuser1aOcdata'
    dbpasswd = 'logawsmaxstrikeuPw2oa&oCdata'
    host = '54.238.211.119'
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    tablegacha = 'cardproduct'
    tablesoul = 'soulproduct'
    print '***********************************'
2100533119
2100227898
2100234249
2100457749
2100386599
2100237237
2100529919
mport pymongo
import json
import sys
import random
import os
import datetime
import time
import traceback2100499712
2100242679
2100246621    
'''
    #findlist = ['2100533119','2100227898','2100234249','2100457749','2100386599','2100237237','2100529919',\
    #'2100499712','2100242679','2100246621']
    
    findlist = ['2100225843','2100362456','2100444907']
    for uid in findlist:
        try:
            #'''
            dblines = db[tablegacha].find({'uid':uid,'where':'timer_gacha','date_time':{'$gt':datetime.datetime(2014,03,17),\
                    '$lt':datetime.datetime(2014,03,20)}})
            #dblines = db[tablegacha].find({'uid':uid,'date_time':{'$gt':datetime.datetime(2014,03,19)}})
            if dblines:
                for dbline in dblines:#try:
                    print 'gachaline', u'时间',dbline['date_time'],'id',dbline['uid'],\
                          u'来自于',dbline['where'],u'卡片的信息',dbline['card_msg']
                    #print '-----------------------------\n',dbline
                #except:
                #    print '******************\n'
            else:
                print '+++++++++++++++++++++++++++++++++\n'
            #'''
            soullines = db[tablesoul].find({'uid':uid,"where" : "award_gift",'date_time':{'$gt':datetime.datetime(2014,03,17),\
                      '$lt':datetime.datetime(2014,03,20)}})
            #soullines = db[tablesoul].find({'uid':uid,'date_time':{'$gt':datetime.datetime(2014,03,19)}})
            if soullines:
                
                for soulline in soullines:#try:
                    #print 'soulline', u'时间',soulline['date_time'],'id',soulline['uid'],u'来自于',soulline['where']
                    print 'soulline is', soulline
                    #print '-----------------------------\n',soulline
                #except:
                #    print '******************\n'
            else:
                print '+++++++++++++++++++++++++++++++++\n'
        except:
            print 'ttttttttttttttllllllllllllll'
if __name__ == '__main__':
    #findlist=['2100409004','2100450596']
    
    dbname = 'logawsmaxstrikedb1a'
    dbauth = 'logawsmaxstrikeuser1aOcdata'
    dbpasswd = 'logawsmaxstrikeuPw2oa&oCdata'
    host = '54.238.211.119'
    '''
    dbname = 'logcnmaxstrikedb1a'
    dbauth = 'logcnmaxstrikeuser1aocdata'
    dbpasswd = 'logcnmaxstrikeuPW1oa&oCdata'
    host = '10.161.177.73'
    ''' 
    port = 27017
    conn = pymongo.Connection(host,port)
    db = eval('conn.%s'%dbname)
    db.authenticate(dbauth,dbpasswd)
    tablegacha = 'cardproduct'
    tablesoul = 'soulproduct'
    print '++++++++++++++++++++++++++++++++++++++ go'
    check(db,tablegacha,tablesoul)
