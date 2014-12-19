# -*- coding: utf-8 -*-
import pymongo
import datetime,traceback,os
import sys
import random
import pymongo
import os
import datetime
import time
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)
from apps.models.user_gift import UserGift
from apps.models.gift_code import GiftCode
from config import Config

class Coin:
      def __init__(self,db,uid):
          self.uid = uid
          self.db = db

      def product(self):
          self.config = Config(self.db,'coinproduct')
          res = self.config.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)
          for i in res:
              if i['where'] == 'award_gift':
                 print 'product' + '-------' + str(i['sum']) + '-------' + str(i['date_time'])[:19]

      def consume(self):
          self.config = Config(self.db,'coinconsume')
          res = self.config.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)
          for i in res:
              print 'consume' + '--------' + str(i['sum']) + '--------' + str(i['date_time'])[:19]

coin = Coin('logawsmaxstrikedb1a','2100216314')
coin.product()
#coin.consume() 
