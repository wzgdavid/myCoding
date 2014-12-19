# -*- coding: utf-8 -*-
import datetime,traceback,os
import sys
import random
import pymongo
import os
import datetime
import time
import pymongo
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)
from apps.models.user_gift import UserGift
from apps.models.gift_code import GiftCode
from config import Config

class Charge:
      def __init__(self,db,param):
         self.db = db 
         self.oid = param['oid']
         if param['uid'] == '':
              print 'uid is no empty'
              self.uid = ''
         else:
              self.uid = param['uid']
         
     
      def record(self):
         self.config = Config(self.db,'chargerecord')
         if self.oid:
            res = self.config.my_table.find({"uid":self.oid}).sort("date_time",pymongo.DESCENDING)
         if self.uid:
            res = self.config.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)
         for i in res:
             print i['oid']

param = {
    'uid':'2100379512',
    'oid':'2999763169054705758.1309460750069851'
}
charge = Charge('logawsmaxstrikedb1a',param)
charge.record()
