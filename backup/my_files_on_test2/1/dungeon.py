#-*- coding: utf-8 -*- 
import datetime,traceback,os
import sys
import random
import pymongo
import os
import datetime
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)
from apps.models.user_dungeon import UserDungeon
from config import Config

class Dungeon: 
     
      def __init__(self,db,uid = ''):
        self.db = db
        if uid == '':
           print 'uid is no empty'
           sys.exit()

      def record(self): 
        self.config = Config(self.db,'dungeonrecord')      
       #res = self.config.my_table.find({"uid":self.uid})
       #list = {}
       #for i in res:
       #    if (i['dungeon_id'] == '7_1' or i['dungeon_id'] == '7_2' or i['dungeon_id'] == '7_3') and i['dungeon_type'] == 'special':
       #        string = i['dungeon_id'] + '------' + i['statament'] + '--------' + str(i['date_time']) 
       #        print string 
    
       

dungeon = Dungeon('logcnmaxstrikedb1a','2100216314')
#dungeon.record()
