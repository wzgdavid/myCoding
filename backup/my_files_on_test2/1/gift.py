# -*- coding: utf-8 -*- 
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
from apps.config import game_config
from config import Config

class Gift:  
      def __init__(self,db,uid):
        self.db = db
        self.uid = uid        
       
      def query(self):
        self.config = Config(self.db,'usergift')
        res = self.config.my_table.find({"uid":self.uid})
        for i in res:
            for m in i['gift_list']:                
                got_time = ''
                upd_time = ''
                if i['gift_list'][m].has_key('got_time'):
                    got_time = time.localtime(i['gift_list'][m]['got_time']) 
                    got_time = time.strftime('%Y-%m-%d %H:%M:%S',got_time)
                if i['gift_list'][m].has_key('upd_time'):                                  
                    upd_time = time.localtime(i['gift_list'][m]['upd_time'])
                    upd_time = time.strftime('%Y-%m-%d %H:%M:%S',upd_time)
                if i['gift_list'][m]['award'].has_key('coin'):
                        value = i['gift_list'][m]['award']['coin']
                if i['gift_list'][m]['award'].has_key('stamina'):
                        value = i['gift_list'][m]['award']['stamina']
                if i['gift_list'][m]['award'].has_key('gold'):
                        value = i['gift_list'][m]['award']['gold']
                if i['gift_list'][m]['award'].has_key('gacha_pt'):
                        value = i['gift_list'][m]['award']['gacha_pt']

               #print i['gift_list'][m]['award'].get('coin')
                print m + '------' + i['gift_list'][m]['content'] + '------' + str(value)  + '------' + got_time + '------' + upd_time
                
       
      def add(self):
       #config = game_config.loginbonus_config      
        user_gift = UserGift.get("1100268619")     
        user_gift.do_put()

      def giftcode(self):
        self.config = Config(self.db,'giftcode')
        res = self.config.my_table.find({"gift_id":"40101"})
        for i in res:
            for m in i['codes']:
                if i['codes'][m] == self.uid:
                    print m

      def coin_gold_item(self):
        self.config_coin = Config(self.db,'coinproduct')
        coin = self.config_coin.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)

        self.config_gold = Config(self.db,'goldproduct')
        gold = self.config_gold.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)

        self.config_item = Config(self.db,'itemproduct')
        item = self.config_item.my_table.find({"uid":self.uid}).sort("date_time",pymongo.DESCENDING)
       
        for i in coin:
           if i['where'] == 'ward_continuous_bonus_record' and str(i['date_time'])[:10] == '2014-03-04':
             print i['uid'] + '------' + str(i['date_time']) + '---------' + str(i['sum']) + '------' + i['where']

        for k in gold:
           if k['where'] == 'award_continuous_bonus_record' and str(k['date_time'])[:10] == '2014-03-04':
             print k['uid'] + '-------' + str(k['date_time']) + '-------' + str(k['sum']) + '-------' + k['where']
        
        for j in item:
           if j['where'] == 'award_month_bonus' and str(j['date_time'])[:10] == '2014-03-02':
             print j['uid'] + '-------' + str(j['date_time']) + '--------' + str(j['sum'])  + '------' + j['where']




      def user_login(self):
        self.config = Config(self.db,'userlogin')
        res = self.config.my_table.find({"uid":self.uid})
        
        n = {}
        t = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        for i in res:
              if i['login_info'].has_key('month_bonus_record'):               
                 for m in i['login_info']['month_bonus_record']['2014-03']['list']:
                    print m,str(i['login_info']['month_bonus_record']['2014-03']['list'][m]['award'])
              if i['login_info'].has_key('continuous_bonus_record'):
                 for h in i['login_info']['continuous_bonus_record']:
                    print h,i['login_info']['continuous_bonus_record'][h]['content']
                                            
gift_1 = Gift('awsmaxstrikedb1a','2100441700')
gift_1.user_login()
gift_2 = Gift('logawsmaxstrikedb1a','2100441700')
gift_2.coin_gold_item()
#gift.query()
#gift.add()
#gift.giftcode()
