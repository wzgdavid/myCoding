# encoding: utf-8
import sys
sys.path.insert(0, '/alidata/sites/stg/qz/')
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

import bisect
import random
import datetime
import copy
from apps.common import utils, tools
from apps.models.user_real_pvp import UserRealPvp
from apps.models.user_base import UserBase
from apps.models import pvp_redis
from apps.oclib import app
from apps.models.user_mail import UserMail
from apps.realtime_pvp import readying_player_redis
from apps.config.game_config import game_config
from apps.models.pvp_redis import get_pvp_redis
from apps.models.user_property import UserProperty
from apps.models.user_gift import UserGift
from apps.models.user_pk_store import UserPkStore
from apps.models.user_equips import UserEquips
from apps.models.user_cards import UserCards
from apps.models.user_pack import UserPack
from apps.models.user_souls import UserSouls
from apps.models import data_log_mod
from common import uid, pprint

game_config.subareas_conf()
game_config.set_subarea('1')

rk_user = UserBase.get(uid)
upk = UserPkStore.get_instance(uid)
#print upk.next_auto_refresh_time
def _pack_store_info(store_info):
    store_info = copy.deepcopy(store_info)
    for each_good_info in store_info["pk_store"]:
        if not isinstance(each_good_info, dict):
            continue
        good_id = each_good_info["goods"]["_id"]
        num = each_good_info["goods"]["num"]
        pack = tools.pack_good(good_id, num)
        each_good_info["goods"] = pack
    return store_info


def get_real_refresh_time():
    user_pk_store = UserPKStore.get_instance(uid)
    print user_pk_store.next_auto_refresh_time
#get_real_refresh_time()


def get_store_info(rk_user, params):
    '''
    获取玩家 pk 商店信息
    '''
    #判断新手引导
    newbie_step = int(params.get('newbie_step', 0))
    if newbie_step:
        rk_user.user_property.set_newbie_steps(newbie_step, "pk_store")
    return _pack_store_info(upk.auto_refresh_store())
#print 'real manual refresh times', UserPkStore.get_instance(uid).manual_refresh_times

#pprint(get_store_info(rk_user, {}))
#pprint(upk.store_info())

def modify_info():
    upk = UserPkStore.get_instance(uid)
    upk.manual_refresh_times = 5
    upk.do_put()
#modify_info()


def refresh_store_by_self():
    '''
    手动刷新 pk 商店
    '''
    upk = UserPkStore.get_instance(uid)
    user_real_pvp = UserRealPvp.get_instance(uid)

    if not upk.can_manual_refresh():
        print 'can_not_refresh'
        return 11, {'msg': utils.get_msg('pk_store','can_not_refresh')}
    # 玩家所拥有的功勋点不够一次刷新
    #refresh_need_honor = game_config.pk_store_config['refresh_need_honor']
    # 玩家所拥有的功勋点不够一次刷新
    refresh_times = str(upk.manual_refresh_times + 1) # 指第几次刷新，第一次刷新时manual_refresh_times 是 0
    refresh_need_honor = game_config.pk_store_config['refresh_need_honor'].get(refresh_times, 1)
    if not user_real_pvp.is_honor_enough(refresh_need_honor):
        return 11, {'msg': utils.get_msg('pk_store','not_enough_honor')}

    user_real_pvp.minus_honor(refresh_need_honor)
    upk.add_refresh_time()
    data = upk.refresh_store_goods()
    user_real_pvp.do_put()
    upk.do_put()
    
    return 0, _pack_store_info(upk.store_info())

print 'refresh_store_by_self()','-'*60
#pprint (refresh_store_by_self())
print 'get_store_info','-'*60
#pprint (get_store_info(rk_user, {}))
#print 'real manual refresh times', UserPkStore.get_instance(uid).manual_refresh_times

def set_refresh_time_to_0():
    '''
    set 0 之后每次进游戏都能自动刷新
    '''
    user_pk_store = UserPkStore.get_instance(uid)
    user_pk_store.next_auto_refresh_time = 0
    user_pk_store.do_put()
#set_refresh_time_to_0()

# 10-14
def test_pk_store_model():
    ups = UserPkStore.get_instance(uid)
    print 'store_info ------ \n',ups.store_info()
    print 'refresh_store_goods ------ \n',ups.refresh_store_goods()
    print 'auto_refresh_store ------ \n',ups.auto_refresh_store()
#test_pk_store_model()

