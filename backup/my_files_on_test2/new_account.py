# encoding: utf-8
from common import uid, qz_path
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
from apps.models.user_real_pvp import UserRealPvp
import json
import copy
import datetime
from apps.common.utils import create_gen_id
from apps.common import utils
import time
from apps.models import data_log_mod
from apps.models import GameModel


game_config.subareas_conf()
game_config.set_subarea('1')

up = UserProperty.get_instance(uid)


def add_honor():
    urp = UserRealPvp.get_instance(uid)
    urp.add_honor(99999)
    urp.do_put()
    print urp.honor

def add_vip_lv():
    user_property = UserProperty.get_instance(uid)
    user_property.add_charge_sumcoin(10)    # vip lv 1
    #user_property.property_info["charge_sumcoin"] = 0     # vip lv 0 
    user_property.do_put() 
#add_vip_lv()

def set_newbie():
    upp = up.property_info
    upp['newbie'] = False 
    upp['newbie_steps'] = 63 
    #upp['stamina'] = 100
    up.do_put()
    print upp['newbie_steps'], upp['newbie']

def set_user_lv():
    up.property_info['lv'] = 40 
    up.do_put()
'''新账号做一些操作，方便调试'''

def add_equip():
    ue = UserEquips.get_instance(uid)
    ue.add_equip('12001_equip')  # 4个装备都是火云套
    ue.add_equip('22001_equip')
    ue.add_equip('32001_equip')
    ue.add_equip('42001_equip')
    ue.add_equip('53003_equip')   # 诗经
    ue.add_equip('63003_equip')   # 沙里飞
    ue.do_put()

def new_account():
    add_equip()
    set_newbie()
    add_honor()
    set_user_lv()
    pass
new_account()
  
