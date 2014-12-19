# encoding: utf-8
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

import time
import copy
import random
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
import json

game_config.subareas_conf()
game_config.set_subarea('1')

def remove_all_equips():
    ue = UserEquips.get_instance(uid)
    ue.equips = {}
    ue.do_put()
#remove_all_equips()



def show_all_equips():
    ue = UserEquips.get_instance(uid)
    pprint(ue.equips)
show_all_equips()

def get_equips_by_card(cid):
    equip_list = []
    ue = UserEquips.get_instance(uid)
    for eid, e_info in ue.equips.items():
        if e_info['used_by'] == cid:
            equip_list.append(eid)
    print equip_list
#get_equips_by_card('2014082f91506056299841')

def get_all_equips_with_fate_card():
    data = {}
    equip_config = game_config.equip_config
    for eid, einfo in equip_config.items():
	if not einfo.get('fate_card'):
	    continue
        data[eid] = einfo
    print data
#get_all_queips_with_fate_card()

def get_fate_by_equip(eid):
    fate_conf = game_config.fate_conf
    for id, info in fate_conf.items():
        if eid in info.get('compose', []):
 	    print id 
#get_fate_by_equip('63003_equip')

def get_card_by_fate(fid):
    card_config = game_config.card_config
    for id, info in card_config.items():
        if fid in info.get('fate_id', []):
            print id
#get_card_by_fate('ch_20108')

'''
14-10-08 看unlock_skill格式
from logics/main.py
'''
def get_equip_config():
    """获得装备的配置
    """
    data = {}
    #获取装备配置信息
    equip_config = copy.deepcopy(game_config.equip_config)
    for eid in equip_config:
        unlock_skill = equip_config[eid].get('unlock_skill',{})
        if unlock_skill:
            #如果有解锁技能的话 就格式化解锁技能
            all_keys = sorted(unlock_skill.keys())
            tmp = []
            for lv in all_keys:
                info = unlock_skill[str(lv)]
                info['lv'] = str(lv)
                tmp.append(info)
            equip_config[eid]['unlock_skill'] = tmp

    data['equip_conf'] = equip_config
    #获取装备等级经验配置信息
    data['equip_exp_conf'] = game_config.equip_exp_conf
    #获取装备强化配置信息
    data['equip_update_config'] = game_config.equip_update_config
    #获取套装配置信息
    data['suit_type_conf'] = game_config.suit_type_conf
    #获取武器的碎片掉落信息
    data['equip_drop_info'] = get_equip_drop_info()
    data['equip_upgrade_config'] = game_config.equip_upgrade_config  # 装备升品配置
    return  data
#print get_equip_config()



def add_equip():
    ue = UserEquips.get_instance(uid)
    #ue.add_equip('12001_equip')  # 4个装备都是火云套
    #ue.add_equip('22001_equip')
    ue.add_equip('35001_equip')
    ue.add_equip('42001_equip')
    #ue.add_equip('53003_equip')   # 诗经
    #ue.add_equip('63003_equip')   # 沙里飞
    ue.do_put()
#add_equip()
#show_all_equips()

def test_is_equip_used():
    uc = UserCards.get_instance(uid)
    print uc.is_equip_used(['201412051105110566880'])
#test_is_equip_used()
