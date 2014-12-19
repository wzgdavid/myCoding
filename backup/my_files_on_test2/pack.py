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
import json
import copy
import datetime
from apps.common.utils import create_gen_id
from apps.common import utils
import time
from apps.models import data_log_mod
from apps.models import GameModel




#uid = '9100214727'
def show_pack_fields():
    user_pack_obj = UserPack.get_instance(uid)
    print 'user_pack_obj.materials','-'*50
    print user_pack_obj.materials
    print 'user_pack_obj.props','-'*50
    print user_pack_obj.props
#show_pack_fields()

def add_props(prop_id,num):
    up = UserPack.get_instance(uid)
    up.add_props(prop_id,num)
    up.do_put()
#add_props('24_props', 99999)

def clear_props(prop_id):
    up = UserPack.get_instance(uid)
    del up.props[prop_id]
    up.do_put()
#clear_props('19_props')

def clear_all_props():
    up = UserPack.get_instance(uid)
    up.props = {}
    up.do_put()
#clear_all_props()

def add_mat():

    up = UserPack.get_instance(uid)
    up.add_material('1_mat',999)
    up.add_material('2_mat',999)
    up.add_material('3_mat',999)
    up.add_material('4_mat',999)
    up.do_put()
#add_mat()

def get_item_config():
    """获得药品的配置
    """
    data = {'item_conf':game_config.item_config}
    data.update(game_config.skill_params_config)
    return 0, data 
#print get_item_config()


