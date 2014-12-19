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
import random
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
print game_config.system_config['recover_stamina_coin']
def show_dungeon_info():
    user_dungeon_obj = UserDungeon.get_instance(uid)
    print 'user_dungeon_obj.dungeon_info','-'*50
    print user_dungeon_obj.dungeon_info
    print 'user_dungeon_obj.dungeon_repeat_info','-'*50
    print user_dungeon_obj.dungeon_repeat_info
    print 'user_dungeon_obj.has_played_info','-'*50
    print user_dungeon_obj.has_played_info
    print 'user_dungeon_obj.dungeon_fail_list','-'*50
    print user_dungeon_obj.dungeon_fail_list 
 
#show_dungeon_info()


def wipe_out():
    '''
    扫荡
    目前只有普通战场有扫荡
    '''
    d_type = 'normal' 
    floor_id = '1'
    room_id  = '1'
    do_times = 1   # 扫荡次数
    data = {}
    if d_type not in ['normal'] or not floor_id or not room_id or do_times not in [1, 10]:
        return 11,{'msg':utils.get_msg('dungeon', 'invalid_params')} # 
    user_dungeon = UserDungeon.get(uid)
    has_played_info = user_dungeon.has_played_info
    '''
    has_played_floor = has_played_info[d_type].get(floor_id)
    # 未达到此战场
    if not has_played_floor:
        return 11,{'msg':utils.get_msg('dungeon', 'not_arrived')} # 
    has_played_room = has_played_floor['rooms'].get(room_id)
    if not has_played_room:
        return 11,{'msg':utils.get_msg('dungeon', 'not_arrived')} # 
    # 没达到3星
    if not has_played_room['perfect']:
        return 11,{'msg':utils.get_msg('dungeon', 'not_three_star')} # 
    '''
    try:
        has_played_info[d_type][floor_id]['rooms'][room_id]
    except:
        return 11,{'msg':utils.get_msg('dungeon', 'not_three_star')}
    # 没达到3星（完美过关）
    if not has_played_info[d_type][floor_id]['rooms'][room_id]['perfect']:
        return 11,{'msg':utils.get_msg('dungeon', 'not_three_star')}
    # 扫荡券不够
    user_pack = UserPack.get_instance(uid)
    if not user_pack.is_props_enough('24_props', do_times):
        return 11,{'msg':utils.get_msg('dungeon', 'wipe_out_not_enough')} # 
    # 目前只有普通战场 
    dungeon_config = game_config.normal_dungeon_config
    room_config = dungeon_config[floor_id]['rooms'][room_id]

    # 计算能够扫荡次数
    can_make_copy_cnt = room_config['can_make_copy_cn']
    if d_type == 'normal':
        try:  #  判断dungeon_repeat_info中有无此关卡记录
            user_dungeon.dungeon_repeat_info[d_type][floor_id][room_id] += 0
        except :
            # 无此关卡记录时，把此关卡今日完成次数置零
            if d_type not in user_dungeon.dungeon_repeat_info:
                user_dungeon.dungeon_repeat_info[d_type]={}
            if floor_id not in user_dungeon.dungeon_repeat_info[d_type]:
                user_dungeon.dungeon_repeat_info[d_type][floor_id] = {}
            if room_id not in user_dungeon.dungeon_repeat_info[d_type][floor_id]:
                user_dungeon.dungeon_repeat_info[d_type][floor_id][room_id] = 0
            user_dungeon.do_put()
    has_played_cnt = user_dungeon.dungeon_repeat_info[d_type][floor_id][room_id]
    can_wipe_out_cnt = can_make_copy_cnt - has_played_cnt
    print can_make_copy_cnt, has_played_cnt 
    # 进入战场次数用完，不能扫荡
    if can_wipe_out_cnt <= 0:
        return 11,{'msg':utils.get_msg('dungeon', 'invalid_limit_dungeon')}
    # 剩余战场次数不够扫荡十次
    if can_wipe_out_cnt < do_times:
        return 11,{'msg':utils.get_msg('dungeon', 'can_not_do_ten_times')}
    # 扫荡战利品
    get_goods = {
        'exp': 0,
        'exp_point': 0,
        'gold': 0,
        'card': {},
        'equip': {},
        'soul':{
            'card': {},
            'equip': {},
        },
        'mat': {},
        'props': {},
    }

    # 扫荡一次能够得到的经验，卡经验点，和钱币
    get_goods['exp'] += room_config.get('exp', 0) * do_times
    get_goods['exp_point'] += room_config.get('exp_point', 0) * do_times
    get_goods['gold'] += room_config.get('gold', 0) * do_times

    # 扫荡能够得到的物品
    drop_info = _pack_drop_info(room_config.get('drop_info', {}))
    invisible_drop = _pack_drop_info(room_config.get('invisible_drop', {}))
    drop_info.extend(invisible_drop)
    # 有掉落物品（包括可见和不可见）时计算掉落, 不用战斗所以不区分可见不可见
    if drop_info: # sample  ['12002_equip', '5_card_soul', '53001_equip_1_soul', '6_card', '23_props', '8_props']
        drop_info = list(set(drop_info))  # list去重
        drop_info_config = game_config.drop_info_config['normal_dungeon']
        # 检查战场掉落配置中是否有此物品
        for goods_id in drop_info:
            print 'goods_id------*--*-*-*-*-*--*-*-*-*-------', goods_id
            if 'soul' in goods_id:
                if goods_id[:-5] not in drop_info_config['soul']:
                    return 11,{'msg':utils.get_msg('dungeon', 'no_this_goods')}
            else:
                if goods_id not in drop_info_config:
                    return 11,{'msg':utils.get_msg('dungeon', 'no_this_goods')}
        # 计算掉落数量
        for n in range(do_times):
            for goods_id in drop_info:
                if 'soul' in goods_id:
                    goods_id = goods_id[:-5]  # 去掉'_soul'后缀
                    value_config = drop_info_config['soul'][goods_id]['visible']
                    # 根据配置概率判断是否得到
                    if utils.is_happen(value_config[1]):
                        num = random.randint(value_config[0][0], value_config[0][1])
                        soul_type = 'card' if 'card' in goods_id else 'equip'
                        if goods_id not in get_goods['soul'][soul_type]:
                            get_goods['soul'][soul_type][goods_id] = num
                        else:
                            get_goods['soul'][soul_type][goods_id] += num
                    else:
                        continue

                else:
                    value_config = drop_info_config[goods_id]['visible']
                    # 根据配置概率判断是否得到
                    if utils.is_happen(value_config[1]):
                        num = random.randint(value_config[0][0], value_config[0][1])
                        for t in ['card', 'equip', 'props', 'mat']:
                            if t in goods_id:
                                get_type = t
                        if goods_id not in get_goods[get_type]:
                            get_goods[get_type][goods_id] = num
                        else:
                            get_goods[get_type][goods_id] += num
                    else:
                        continue
    # 减扫荡券
    user_pack = UserPack.get_instance(uid)
    user_pack.minus_props('24_props', do_times, 'wipe_out')
    # 添加扫荡奖励
    user_property = UserProperty.get_instance(uid)
    tmpdata = user_property.test_give_award(get_goods, where='wipe out')
    user_property.do_put()
    uc = UserCards.get_instance(uid)
    uc.do_put()
    ue = UserEquips.get_instance(uid)
    ue.do_put()
    up = UserPack.get_instance(uid)
    up.do_put()
    us = UserSouls.get_instance(uid)
    us.do_put()
    # 记录repeat info
    user_dungeon.add_repeat_cnt(d_type, floor_id, room_id, do_times)
    user_dungeon.do_put()

    # 给前端
    data['get_exp'] = tmpdata['exp']
    data['get_exp_point'] = tmpdata['exp_point']
    data['get_gold'] = tmpdata['gold']
    data['get_card'] = tmpdata['card']
    data['get_equip'] = tmpdata['equip']
    data['get_souls'] = tmpdata['soul']
    data['get_material'] = tmpdata['mat']
    data['get_props'] = tmpdata['props']

    print data

def _pack_drop_info(drop_info):
    '''
    把drop_info转换成一个list
    '''
    rtn_list = []
    for goods_type in drop_info:
        if goods_type == 'soul':
            # 如果是碎片，后缀'_soul'以示区别
            rtn_list.extend([goods_id+'_soul' for goods_id in drop_info[goods_type]])
        else:
            rtn_list.extend(drop_info[goods_type])
    return rtn_list


#print wipe_out()

from apps.logics import dungeon
