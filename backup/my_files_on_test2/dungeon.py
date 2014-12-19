# encoding: utf-8
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

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
from apps.models.collection import UserCollection
import json
import copy
import datetime
from apps.common.utils import create_gen_id
from apps.common import utils
import time
from apps.models import data_log_mod
from apps.models import GameModel
from apps.logics import vip
from apps.common.exceptions import GameLogicError

user = UserBase.get(uid)
game_config.subareas_conf()
game_config.set_subarea('1')


def reset_repeat_info():
    '''
    10-20
    做扫荡功能时
    '''
    user_dungeon = UserDungeon.get_instance(uid)
    user_dungeon.recover_copy('normal', '1', '2')
    user_dungeon.do_put()
#reset_repeat_info()

def modify_today_str():
    ud = UserDungeon.get_instance(uid)
    ud.dungeon_repeat_info['today_str'] = '2014-11-23'
    ud.do_put()
#modify_today_str()
        
def recover_test():
    vip_lv = 1
    user_dungeon = UserDungeon.get_instance(uid)    
    vip_conf = game_config.user_vip_conf
    user_config = vip_conf.get(str(vip_lv),{})    


def get_recover_times():
    while True:
        data = {}
        all_dungeon = ['normal','daily','special']
        #获取vip等级
        up = UserProperty.get_instance(uid)
        vip_lv = up.vip_cur_level
        vip_conf = game_config.user_vip_conf
        user_config = vip_conf.get(str(vip_lv),{})
        today_str = utils.get_today_str()
        recover_list = ['recover_stamina','recover_pvp_stamina','recover_mystery_store']
        recover_times = up.property_info['recover_times']
        if recover_times['today_str'] == today_str:
            for recover in recover_list:
                data[recover] = user_config['can_'+recover+'_cnt'] - recover_times[recover]
            data['recover_copy'] = {}
            for i in all_dungeon:
                data['recover_copy'][i] = user_config['can_recover_copy_cnt'][i]  - recover_times['recover_copy'][i]
        else:
            up.reset_recover_times()
            data = self.property_info['recover_times']
        return data

#print get_recover_times()

def test_get_recover_times():
    #uid = '56100214959'
    up = UserProperty.get_instance(uid)
    print up.get_recover_times()
#test_get_recover_times()

def reset_recover_times():
    up = UserProperty.get_instance(uid)
    up.reset_recover_times()
    up.do_put()
#reset_recover_times()

def test_add_recover_times():
    up = UserProperty.get_instance(uid)
    up.add_recover_times('recover_copy', 'normal')
    up.do_put()
#test_add_recover_times()

def print_times():
    up = UserProperty.get_instance(uid)
    print "up.property_info['recover_times']['recover_copy']",'-'*50
    print up.property_info['recover_times']['recover_copy']  # 当天用掉的次数
    print up.property_info['recover_times']
#print_times()


def recover_copy():
    """
    * 重置副本次数
    """
    rk_user = UserBase.get(uid)
    recover_copy_coin = game_config.system_config['recover_copy_coin']
    #检查vip可以回复的次数到了没
    if not vip.check_limit_recover(rk_user,'recover_copy'):
        return 11,{'msg':utils.get_msg('user','max_recover_copy_times')}
    else:
        try:
            #检测参数是否合法
            dungeon_type = 'normal' 
            floor_id = '1' 
            room_id  = '1' 
        except:
            return 11,{'msg':utils.get_msg('dungeon','invalid_dungeon_info')}
        #检查用户coin是否足够
        if not rk_user.user_property.minus_coin(recover_copy_coin, 'recover_copy'):
            return 11,{'msg':utils.get_msg('user','not_enough_coin')}
        #添加回复次数
        rk_user.user_property.add_recover_times('recover_copy',dungeon_type)
        user_dungeon_obj = UserDungeon.get(rk_user.uid)
        user_dungeon_obj.recover_copy(dungeon_type,floor_id,room_id)

        rk_user.user_property.do_put()
        user_dungeon_obj.do_put()
        return 0,{}
#print recover_copy()


#show_dungeon_info()


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


def wipe_out(rk_user, params):
    '''
    扫荡
        玩家能够在已经完美过关的关卡上使用扫荡功能，扫荡不用进入战斗画面，直接返回关卡奖励
        与普通战斗不同的是扫荡并不需要更新战场的关卡信息，
    params: 
        dungeon_type:'normal'  战场类型，有普通战场 normal , 试炼 daily
        floor_id:'1'
        room_id:'1'
        do_times: '1'  扫荡次数
    '''     
    d_type = params.get('dungeon_type')
    floor_id = params.get('floor_id')
    room_id  = params.get('room_id')
    do_times = params.get('do_times')   # 扫荡次数
    # ------------------------------参数check start-------------------------
    if d_type not in ['normal', 'daily'] or not floor_id or not room_id:
        return 6, {'msg':utils.get_msg('dungeon', 'invalid_params')}
    try:
        do_times = int(do_times)
    except ValueError:
        return 6, {'msg':utils.get_msg('dungeon', 'invalid_params')}
    if do_times <= 0:
        return 6, {'msg':utils.get_msg('dungeon', 'invalid_params')}
    user_dungeon = rk_user.user_dungeon
    has_played_info = user_dungeon.has_played_info
    user_property = rk_user.user_property
    # 读配置
    conf_dict = {
        'normal': game_config.normal_dungeon_config,
        'daily': game_config.daily_dungeon_config
    }
    dungeon_config = conf_dict[d_type]
    # 战场不存在 
    try:
        dungeon_config[floor_id]['rooms'][room_id]
    except KeyError:
        return 6,{'msg':utils.get_msg('dungeon', 'invalid_dungeon')}
    # ------------------------------参数check end----------------------------

    # ------------------------------扫荡逻辑check start----------------
    # 玩家未达到15级，不开启扫荡
    open_lv = game_config.user_init_config['open_lv'].get('wipe_out', 0)
    if user_property.lv < open_lv:
        return 11,{'msg':utils.get_msg('dungeon', 'wipe_out_open_lv') % open_lv}
    # vip未达到4级，不开启多次扫荡
    open_lv = game_config.user_init_config['open_lv'].get('vip_multi_wipe_out', 0)
    if do_times > 1 and user_property.vip_cur_level < open_lv:
        return 11,{'msg':utils.get_msg('dungeon', 'vip_wipe_out') % open_lv}

    floor_config = dungeon_config[floor_id]
    room_config = dungeon_config[floor_id]['rooms'][room_id]
    # 未达到此战场
    try:
        has_played_info[d_type][floor_id]['rooms'][room_id]
    except KeyError:
        return 11,{'msg':utils.get_msg('dungeon', 'not_arrived')}
    # 没达到3星
    if not has_played_info[d_type][floor_id]['rooms'][room_id]['perfect']:
        return 11,{'msg':utils.get_msg('dungeon', 'not_three_star')}
    # 当前扫荡券不足
    user_pack = rk_user.user_pack
    if not user_pack.is_props_enough('24_props', do_times):
        return 11,{'msg':utils.get_msg('dungeon', 'wipe_out_not_enough')}

    # 检查用户体力是否足够
    #need_stamina = int(room_config['stamina']) * do_times
    #if user_property.stamina < need_stamina:
    #    raise GameLogicError('user','not_enough_stamina')
    
    # 进入战场次数用完，不能扫荡,  或者更新repeat_info的当天日期
    if user_dungeon.check_limit_dungeon(rk_user,params) is False:
        raise GameLogicError('dungeon', 'invalid_limit_dungeon')
    # 计算能够扫荡次数
    
    if d_type == 'normal':
        try:  #  判断dungeon_repeat_info中有无此关卡记录
            user_dungeon.dungeon_repeat_info[d_type][floor_id][room_id]
        except KeyError:
            # 无此关卡记录时，把此关卡今日完成次数置零
            user_dungeon.dungeon_repeat_info      \
                .setdefault(d_type, {})           \
                .setdefault(floor_id, {})         \
                .setdefault(room_id, 0)
            user_dungeon.put()
        can_make_copy_cnt = room_config['can_make_copy_cn']
        has_played_cnt = user_dungeon.dungeon_repeat_info[d_type][floor_id][room_id]
    elif d_type == 'daily':
        try:  #  判断dungeon_repeat_info中有无此关卡记录
            user_dungeon.dungeon_repeat_info[d_type][floor_id]
        except KeyError:
            # 无此关卡记录时，把此关卡今日完成次数置零
            user_dungeon.dungeon_repeat_info      \
                .setdefault(d_type, {})           \
                .setdefault(floor_id, 0)
            user_dungeon.put()
        can_make_copy_cnt = floor_config['can_make_copy_cn']
        has_played_cnt = user_dungeon.dungeon_repeat_info[d_type][floor_id]

    
    can_wipe_out_cnt = can_make_copy_cnt - has_played_cnt

    data = {}
    # 剩余战场次数不够扫荡n次
    if can_wipe_out_cnt < do_times:
        return 11,{'msg':utils.get_msg('dungeon', 'cant_do_multi_times') % do_times}
    data['can_wipe_out_cnt'] = can_wipe_out_cnt
    # ------------------------------扫荡逻辑check end----------------

    # 能扫荡次数和vip等级有关
    #if utils.get_today_str() == user_property.property_info['recover_times']['today_str']:
    #    wipe_out_times = user_property.property_info.get('wipe_out_times', 0)
    #    vip_lv = user_property.vip_cur_level
    #    can_wipe_out_cnt = game_config.user_vip_config[str(vip_lv)]['can_wipe_out_cnt']
    #    if can_wipe_out_cnt - wipe_out_times < do_times:
    #        return 11,{'msg':utils.get_msg('dungeon', 'vip_wipe_out')}
    #    user_property.property_info['wipe_out_times'] += do_times
    #else:
    #    user_property.property_info['wipe_out_times'] = do_times
    #    vip.check_limit_recover(rk_user, 'wipe_out')  # 更新一下，防止出错
    #user_property.put()

    # ------------------------------添加扫荡物品 start----------------
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
                        if 'card' in goods_id:
                            soul_type = 'card'
                        else:
                            soul_type = 'equip'
                     
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

    # 添加must_drop必掉物品
    md = room_config.get('must_drop', {})
    for goods_type in md:
        if goods_type == 'soul':
            for key in md[goods_type]:
                if 'card' in key:
                    soul_type = 'card'
                elif 'equip' in key:
                    soul_type = 'equip'
                if key in get_goods[goods_type][soul_type]:
                    get_goods[goods_type][soul_type][key] += md[goods_type][key]
                else:
                    get_goods[goods_type][soul_type][key] = md[goods_type][key]
        else:
            for key in md[goods_type]:
                if key in get_goods[goods_type]:
                    get_goods[goods_type][key] += md[goods_type][key]
                else:
                    get_goods[goods_type][key] = md[goods_type][key]

    # ------------------------------添加扫荡物品 end----------------

    # 添加扫荡获得奖励
    tmpdata = user_property.test_give_award(get_goods, where='wipe_out')
    user_property.do_put()
    # 减扫荡券
    user_pack.minus_props('24_props', do_times, 'wipe_out')
    user_pack.do_put()
    # 扣体力
    #user_property.minus_stamina(need_stamina)
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

    return 0, data

params = {'dungeon_type':'normal', 'floor_id':'1', 'room_id':'1', 'do_times':'1'}
pprint(wipe_out(user, params))
params = {'dungeon_type':'daily', 'floor_id':'1', 'room_id':'1', 'do_times':'1'}
#pprint(wipe_out(user, params))

def modify_daily():
    '''做试炼扫荡时'''
    ud = UserDungeon.get_instance(uid) 
    ud.has_played_info['daily']['1']['rooms']['1']['perfect'] = True 
    ud.do_put()
#modify_daily()


def show_dungeon_info():
    user_dungeon_obj = UserDungeon.get_instance(uid)

    #user_dungeon_obj.dungeon_repeat_info = {'today_str': '2014-11-16', 'special': {}, 'daily': {}, 'normal': {}}
    user_dungeon_obj.do_put()

    print 'user_dungeon_obj.dungeon_info','-'*50
    pprint(user_dungeon_obj.dungeon_info)
    print 'user_dungeon_obj.dungeon_repeat_info','-'*50
    pprint (user_dungeon_obj.dungeon_repeat_info)
    print 'user_dungeon_obj.has_played_info','-'*50
    pprint(user_dungeon_obj.has_played_info)
    print 'user_dungeon_obj.dungeon_fail_list','-'*50
    #pprint(user_dungeon_obj.dungeon_fail_list) 
 
#show_dungeon_info()
