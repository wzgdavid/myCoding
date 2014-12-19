import sys
import random
import pymongo
import os
import datetime
import time

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
