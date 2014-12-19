# encoding: utf-8
"""
filename:user_login.py
"""
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import datetime,time
import copy
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)
from apps.common import utils
from apps.models.user_base import UserBase
from apps.models.user_cards import UserCards
from apps.models.user_property import lv_top_model
from apps.models.user_login import UserLogin

from apps.models import GameModel

from apps.logics.main import index

import bisect
import random

from apps.models.user_real_pvp import UserRealPvp
from apps.models import pvp_redis
from apps.oclib import app

from apps.realtime_pvp import readying_player_redis
from apps.config.game_config import game_config

game_config.subareas_conf()
game_config.set_subarea('1')
ul = UserLogin.get_instance(uid)
user = UserBase.get(uid)

#pprint(index(user,{})[1])

def show_login_info():
    ul = UserLogin.get_instance(uid)
    pprint(ul.login_info)

    #print ub.add_time
    #del ul.login_info['login_record_new']
    #ul.do_put()
show_login_info() 

def modify():
    #ul.login_info['total_login_num'] = 3
    #ul.login_info['login_time'] = 1415855580    # 2014 11 13

    ul.do_put()    
#modify()

def login():
    ul = UserLogin.get_instance(uid)
    params = {}
    pprint(ul.login(params))
    #ul.do_put()
#login()
#show_login_info() 

def see_award():
    ul = UserLogin.get_instance(uid)
    print ul.get_daily_login_award()
    print ul.get_continuous_login_award(ul.login_info['continuous_login_num'])
    #print ul.login_info['continuous_login_num']
    print ul.get_total_login_award(str(ul.login_info['total_login_num']))
    print ul.login_info['total_login_num']
#see_award()

def modify_login_record_new():
    ul = UserLogin.get_instance(uid)  # 2014-12-05 09:27:55
    print ul.login_info['login_record_new']
    ul.login_info['login_record_new'][0] = '2014-12-01 09:27:55'
    ul.do_put()
#modify_login_record_new()

def test_month_total_login():
    ul = UserLogin.get_instance(uid) 
    print ul.month_total_login
test_month_total_login()
