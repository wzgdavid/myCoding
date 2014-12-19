# encoding: utf-8
from common import uid, qz_path
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

import bisect
import random
import datetime
from apps.common import utils
from apps.models.user_real_pvp import UserRealPvp
from apps.models.user_base import UserBase
# from apps.models.user_property import UserProperty
# from apps.models.friend import Friend
from apps.models import pvp_redis
from apps.oclib import app
from apps.models.user_mail import UserMail
from apps.realtime_pvp import readying_player_redis
from apps.config.game_config import game_config
from apps.models.pvp_redis import get_pvp_redis
from apps.models.user_property import UserProperty
from apps.models.user_gift import UserGift
from apps.models.user_souls import UserSouls
game_config.subareas_conf()
game_config.set_subarea('1')
us = UserSouls.get_instance(uid)

def clear_equip_souls():
    us.equip_souls_info = {}
    us.do_put()
#clear_equip_souls()

def clear_card_souls():
    us.normal_souls = {}
    us.do_put()
#clear_card_souls()

def show_card_souls():
    us = UserSouls.get_instance(uid)
    print us.normal_souls
#show_card_souls()

def show_equip_souls():
    us = UserSouls.get_instance(uid)
    print us.equip_souls_info
show_equip_souls()
#clear_equip_souls()
