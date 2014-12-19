#-*- coding: utf-8 -*-
import sys
import random
import pymongo
import os
import datetime
import time
import traceback
import json
tablesdict = {'1':'buildupdate',
    '2':'cardconsume',
    '3':'carddeck',
    '4':'cardproduct',
    '5':'cardupdate',
    '6':'cardupgrade',
    '7':'chargerecord',
    '8':'chargeresultlog',
    '9':'coinconsume',
    '10':'coinproduct',
    '11':'consumerecord',
    '12':'dungeonrecord',
    '13':'equconsume',
    '14':'equproduct',
    '15':'feed',
    '16':'goldconsume',
    '17':'goldproduct',
    '18':'huntrecord',
    '19':'invite',
    '20':'itemconsume',
    '21':'itemproduct',
    '22':'loginrecord',
    '23':'matconsume',
    '24':'matproduct',
    '25':'miorderidrecord',
    '26':'newguide',
    '27':'pvprecord',
    '28':'soulconsume',
    '29':'soulproduct',
    '30':'stoneconsume',
    '31':'stoneproduct',
    '32':'system.indexes',
    '33':'system.users',
    '34':'userlevelhistory',
}
class Config:
      con = None
      my_db = None
      my_table = None
      def __init__(self,db,tbl):
        self.port = 27017
        if db == 'logcnmaxstrikedb1a' or db == 'cnmaxstrikedb1a':
           self.host = '10.161.177.73:27017'
           Config.con = pymongo.Connection(self.host,self.port)
           Config.my_db = eval('Config.con.%s' % db)
           if db == 'logcnmaxstrikedb1a':
              Config.my_db.authenticate('logcnmaxstrikeuser1aocdata','logcnmaxstrikeuPW1oa&oCdata')
           if db == 'cnmaxstrikedb1a':
              Config.my_db.authenticate('cnmaxstrikeuser1aocdata','cnmaxstrikeuPwD1&aooCdata')
           Config.my_table = eval('Config.my_db.%s' % tbl)
        elif db == 'logawsmaxstrikedb1a' or db == 'awsmaxstrikedb1a':
           self.host = '54.238.211.119:27017'
           Config.con = pymongo.Connection(self.host,self.port)
           Config.my_db = eval('Config.con.%s' % db)
           if db == 'logawsmaxstrikedb1a':
              Config.my_db.authenticate('logawsmaxstrikeuser1aOcdata','logawsmaxstrikeuPw2oa&oCdata')
           if db == 'awsmaxstrikedb1a':
              Config.my_db.authenticate('awsmaxstrikeuse1aocdata','awsmaxstrikeupwD1&aooCdata')
           Config.my_table = eval('Config.my_db.%s' % tbl)

def getdb():
    print("please input the db you use")
    print('***********************************************')
    print('enter 1 for logcnmaxstrikedb1a')
    print('enter 2 for logawsmaxstrikedb1a')
    print('enter 3 for cnmaxstrikedb1a')
    print('enter 4 for awsmaxstrikedb1a')
    print('exit 0')
    dbhost = raw_input('the db want to connect   \n    ')
    print dbhost + 'you type'
    port = 27017
    if dbhost=='1' or dbhost=='3':
        host = '10.161.177.73'
        conn = pymongo.Connection(host,port)
        if dbhost=='1':
            dbname = 'logcnmaxstrikedb1a'
            dbauth = 'logcnmaxstrikeuser1aocdata'
            dbpasswd = 'logcnmaxstrikeuPW1oa&oCdata'
        else:
            dbname = 'cnmaxstrikedb1a'
            dbauth = 'cnmaxstrikeuser1aocdata'
            dbpasswd = 'cnmaxstrikeuPwD1&aooCdata'
    elif dbhost=='2' or dbhost=='4':
        host = '54.238.211.119'
        conn = pymongo.Connection(host,port)
        if dbhost=='2':
            dbname = 'logawsmaxstrikedb1a'
            dbauth = 'logawsmaxstrikeuser1aOcdata'
            dbpasswd = 'logawsmaxstrikeuPw2oa&oCdata'
        else:
            dbname = 'awsmaxstrikedb1a'
            dbauth = 'awsmaxstrikeuse1aocdata'
            dbpasswd = 'awsmaxstrikeupwD1&aooCdata'
    else:
        print 'you type wrong please do again'
        dbhost=''
    if dbhost:
        db = eval('conn.%s'%dbname)
        db.authenticate(dbauth,dbpasswd) 
    else:
        db = ''
    return db
def printkv(k,v,ok):

    ''' ***********  打印输出key和value   *********** '''
    if isinstance(v,dict):
        for myk,myv in v.items():
            opstr = ok+'->'+myk
            #print opstr            
            printkv(myk,myv,opstr)
    else:
        print ' --- %s     %s ---' %(ok,v)

if __name__ == '__main__':
    mydb = getdb()
    if mydb:
        # print  mydb.buildupdate.find_one()
        print 'DB connection OK please do your action\n'
        print('please input the table you want to check\n')
        for k,v in tablesdict.items():
            print k,v
        flag = 1
        while flag:
            checktable = raw_input('please input the table you want operation\n')
            uid = raw_input('please input the user id \n')
            if checktable.isdigit() == False:
                print 'you type wrong number\n'
            elif int(checktable)>32 or int(checktable)<1:
                print 'the number you type is wrong\n'
            else:
                try:
                    table = tablesdict[checktable]
                    if uid:
                        pass
                    else:
                        uid = '1100254414'
                    dbline = mydb[table].find({'uid':uid})[0]
                    print dbline
                    for k,v in dbline.items():
                        '''                        mykey = k
                        valueisdic = isinstance(v,dict)
                        if valueisdic:
                            while valueisdic:
                                mykey
                        else:
                            print 'key is****  %s ****** and value is %s' %(k,v)
                        '''
                        printkv(k,v,k)
                    #print json.dumps(dbline,indent=4)
                    flag = 0
                    break
                except:
                    traceback.print_exc()
                    pass
        #coll = mydb.checktable.findOne()
        #print coll
        
    else:
        print 'EXIT'
