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

class Card:
      def __init__(self,db,uid):
         self.db = db
         self.uid = uid

      def product(self):
         self.config = Config(self.db,'cardproduct')
         res = self.config.my_table.find({"uid":self.uid})
         '''
         name = '高览'
         for i in res:
                k = i['card_msg']['name']             
                w = k.encode('utf-8')
                t = w.split('·')                
                if len(t) == 2:
                   if t[1] == name:
                      print i['uid'] + '-----' + i['card_msg']['name'] + '------' + str(i['date_time'])[:19] + '--------' + i['where'] + '------' + 'yes'
                   else:
                      print i['uid'] + '-----' + i['card_msg']['name'] + '------' + str(i['date_time'])[:19] + '--------' + i['where']
               #if i['where'] == 'gacha_charge':
               #print i['card_msg']['name'] + '------' + str(i['date_time'])[:19]
         '''
         for i in res:
              #if i['card_msg']['star'] == "5":
               if i['where'] == "gacha_charge":
                   print i['uid'] + '-----' + i['card_msg']['name'] + '------' + str(i['date_time'])[:19] + '--------' + i['where'] + '------' + i['card_msg']['star'] 
               

      def update(self):
         self.config = Config(self.db,'cardupdate')
         res = self.config.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)
         name = '魏延'.decode('utf-8')        
         for i in res: 
             #if i['card_msg']['name'] == name:
               print i['card_msg']['name'] + '-------' + str(i['date_time'])[:19] + '--------' + str(i['card_msg']['exp']) + '----------' + i['where']
            

      def consume(self):
         self.config = Config(self.db,'cardconsume')
         res = self.config.my_table.find({"uid":self.uid})
          
         
         name = '高览'
         for i in res:
             k = i['card_msg']['name']
             w = k.encode('utf-8')                          
             t = w.split('·')             
             if len(t) == 2:
                 if t[1] == name:
                    print i['uid'] + '------' + i['card_msg']['name'] + '------' + str(i['date_time'])[:19] + '--------' + i['where'] + '------' + 'yes'
                 else:
                    print i['uid'] + '------' + i['card_msg']['name'] + '------' + str(i['date_time'])[:19] + '--------' + i['where']
            #elif len(t) == 1:
            #print i['card_msg']['name'] + '------' + str(i['date_time'])[:19] + '--------' + i['where']

         '''
         for i in res:
             if i['where'] == 'sell_card':
                print i['card_msg']['name'] + '-------'+ str(i['date_time'])[:19] + '------' + i['where']
            #if i['where'] == 'card_update':
            #   print  str(i['date_time'])[:19] + '------' + i['where']
         '''

card = Card('logawsmaxstrikedb1a','2100455982')
#card.consume()
card.product()
#card.update()
