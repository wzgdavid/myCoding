# encoding: utf-8
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)


from apps.models.user_gift import UserGift
from apps.models.user_login import UserLogin
from apps.models.user_base import UserBase
from apps.config.game_config import game_config
from apps.models.user_cards import UserCards
from apps.models.user_property import UserProperty
from apps.models.user_dungeon import UserDungeon
from apps.models.user_pack import UserPack
from apps.models.user_property import UserProperty
from apps.models.user_equips import UserEquips
from apps.models.collection import UserCollection
from apps.models.user_souls import UserSouls
import json
import copy
import datetime
from apps.common.utils import create_gen_id
from apps.common import utils
import time
from apps.models import data_log_mod
from apps.models import GameModel


#uid = '9100214781'
game_config.subareas_conf()
game_config.set_subarea('1')

up = UserProperty.get_instance(uid)
pprint(up.property_info)
def show_property_fields():
    user_property_obj = UserProperty.get_instance(uid)
    print 'user_property_obj.property_info','-'*50
    pprint(user_property_obj.property_info)
    #user_property_obj.property_info['wipe_out_times'] = 0
    #user_property_obj.do_put()
    '''
    print 'user_property_obj.charge_award_info','-'*50
    print user_property_obj.charge_award_info
    print 'user_property_obj.consume_award_info','-'*50
    print user_property_obj.consume_award_info
    print 'user_property_obj.month_item_info','-'*50
    print user_property_obj.month_item_info
    '''
show_property_fields()

def modify_today_str():
    up.property_info['recover_times']['today_str'] = '2014-11-15'
    up.do_put()
#modify_today_str()

def add_stamina():
    up.add_stamina(100)
    up.do_put()
#add_stamina()

def t_give_award():
    user_property_obj = UserProperty.get_instance(uid)
    user_property_obj.give_award({'gold':3})
    user_property_obj.do_put()
#t_give_award()


def property_real_pvp():
    user_property_obj = UserProperty.get_instance(uid)
    user_real_pvp = user_property_obj.user_base.user_real_pvp
    print user_real_pvp
#property_real_pvp()


def ttest_give_award():
    user_property = UserProperty.get_instance(uid)
    uc = UserCards.get_instance(uid) 
    ue = UserEquips.get_instance(uid) 
    up = UserPack.get_instance(uid)
    us = UserSouls.get_instance(uid) 
    #award = {'card':{'1_card':1}}
    #award = {'equip':{'13001_equip': 2}}
    #award = {'props':{'1_props':2}}
    #award = {'soul':{'card':{'1_card':1}}}
    award = {'soul':{'equip':{'13001_equip':1}}}
    print user_property.test_give_award(award)
    uc.do_put()   
    ue.do_put()
    up.do_put()
    us.do_put()
#ttest_give_award()
        
def add_vip_lv():
    user_property = UserProperty.get_instance(uid)
    user_property.add_charge_sumcoin(10)    # vip lv 1
    #user_property.property_info["charge_sumcoin"] = 0     # vip lv 0 
    user_property.do_put() 
#add_vip_lv()

def modify_vip_lv(lv):
    '''vip等级是通过玩家充值元宝的总数来判断的，没vip等级这个字段，所以是间接改'''
    vip_conf = game_config.user_vip_config[str(lv)] 
    coin = vip_conf['coin']
    up = UserProperty.get_instance(uid)
    #up.add_charge_sumcoin(coin)
    up.property_info["charge_sumcoin"] = coin
    up.do_put()
#modify_vip_lv(1)

def set_newbie():
    upp = up.property_info
    #upp['newbie'] = False 
    #upp['newbie_steps'] = 63 
    #upp['stamina'] = 100
    up.do_put()
    print upp['newbie_steps'], upp['newbie']
#set_newbie()

def get_info():
    print up.property_info
    print up.vip_cur_level
#get_info()  
  
def modify_attr():
    up = UserProperty.get_instance(uid)
    up.property_info['lv'] = 43
    up.do_put()
#modify_attr()
