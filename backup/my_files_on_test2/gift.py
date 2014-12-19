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
import json
import copy
import datetime
from apps.common.utils import create_gen_id
from apps.common import utils, tools
import time
from apps.models import data_log_mod
from apps.models import GameModel
ug = UserGift.get_instance(uid)

rk_user = UserBase.get(uid)
ul = rk_user.user_login
def show_gift():
    ug = UserGift.get_instance(uid)
    pprint(ug.gift_list)

def add_gift():
    ug = UserGift.get_instance(uid)
    ug.add_open_server_gift({'gold': 50, '1_card':1}, 8)
    ug.do_put()

#add_gift()

def get_gift():
    ug.get_gift('2')
    ug.do_put()
#get_gift()
#show_gift()

def clear_all_gifts():
    ug.gift_list = {}
    ug.do_put()
#clear_all_gifts()

def clear_open_server():
    
    #print(ug.open_server_record)
    #ug.clear_open_server_gift()
    #ug.do_put()
    print(ug.open_server_record)
#clear_open_server()


def _got_days(ug):
    '''已领取开服奖励的天数'''
    days = 0
    for info in ug.open_server_record['gifts'].values():
        if info['has_got']:
            days += 1
    return days

def show_open_server_gift(rk_user, params):
    '''
    返回开服奖励的礼包
    '''
    ug = rk_user.user_gift
    ul = rk_user.user_login
    add_time = utils.timestamp_toDatetime(rk_user.add_time)
    now = datetime.datetime.now()
    today = utils.get_today_str()
    # 初始化
    if not ug.open_server_record:
        # 'gifts'按领取天数记录奖励是否领取，比如登录过10天，但只领过一次，这时gifts记录的是['1']['has_got']=True ,其他为False
        # 因为每天只能领取一次，'date_info'用来按日期记录哪天是否已领过一次
        ug.open_server_record = {'gifts': {}, 'date_info': {}}
        for day in range(1, 32):
            ug.open_server_record['gifts'].setdefault(str(day), {})['has_got'] = False
        ug.do_put()
    # 账号注册已达45天（包括注册当天），或者全部领取了，则清空全部开服礼包
    if (now - add_time).days + 1 > 45 or ug.has_got_all_open_server_gifts():
        ug.clear_open_server_gift()
        return 11, {'msg': utils.get_msg('gift','clear_open_server')}
    awards = game_config.loginbonus_config['open_server_gift'].get('awards', {})
    data = {'gifts': {}}
    for days, award in awards.items():
        data['gifts'].setdefault(days, {})['awards'] = award
        #data['gifts'][days]['has_got'] = ug.open_server_record.setdefault(days, {}).setdefault('has_got', False)
        data['gifts'][days]['has_got'] = ug.open_server_record['gifts'][days]['has_got']
        # 给前端现实能否领取，不需存在model中
        #data['gifts'][days]['can_get'] = True if ul.total_login_num >= int(days) else False
        if int(days) == _got_days(ug)+1 and not ug.open_server_record['date_info'].get(today, False):
            data['gifts'][days]['can_get'] = True
        else:
            data['gifts'][days]['can_get'] = False 
    ug.do_put()
    return 0, data
#pprint(show_open_server_gift(rk_user, {}))

def get_open_server_gift(rk_user, params):
    '''
    领取开服礼包中的奖励
    参数
        params['day'] 第几次领
    '''
    #day = params['day']
    day = '5'
    ug = rk_user.user_gift
    ul = rk_user.user_login
    awards = game_config.loginbonus_config['open_server_gift'].get('awards', {})
    if day not in awards.keys():
        return 11, {'msg': utils.get_msg('gift', 'gift_not_exist')}
    the_gift = ug.open_server_record['gifts'][day]
    if the_gift['has_got']:
        return 11, {'msg': utils.get_msg('gift', 'gift_has_got')}
    today = utils.get_today_str()
    if ug.open_server_record['date_info'].get(today, False):
        return 11, {'msg': utils.get_msg('gift', 'today_has_signed_in')}
    # 按顺序领取
    if int(day) != _got_days(ug)+1:
        return 11, {'msg': utils.get_msg('gift', 'signin_in_turn')}
    data = tools.add_things(
        rk_user, 
        [{"_id": goods, "num": awards[goods]} for goods in awards if goods],
        where="open_server_gift"
    )
    the_gift['has_got'] = True
    # 因为每天只能领取一次，'date_info'用来按日期记录哪天是否已领过一次
    ug.open_server_record['date_info'][today] = True 
    ug.do_put()
    return 0, data
#print('get_open_server_gift(rk_user, {})')
#pprint(get_open_server_gift(rk_user, {}))
#print('show_open_server_gift(rk_user, {})')
#pprint(show_open_server_gift(rk_user, {}))

def test_clear_open_server_gift():
    ug.clear_open_server_gift()
    ug.do_put()
#test_clear_open_server_gift()

def test_init_open_server_gift():
    ul.init_open_server_gift()
    ug.do_put() 
#test_init_open_server_gift()

def test_has_got_today_gift():
    return ug.has_got_today_open_server_gift()
#print 'has got: ',test_has_got_today_gift()

def _get_total_sign_in_days(ug):
    days = 0
    for info in ug.sign_in_record.values():
        if info['has_got']:
            days += 1
    return days

def get_sign_in_gift(rk_user, params):
    '''
    领取签到奖励
    params['day'] 当月日期，作为id使用
    '''
    day = '5' 
    ug = rk_user.user_gift
    now = datetime.datetime.now()
    month = str(now.month)
    today = str(now.day)
    print ' _get_total_sign_in_days(ug)',  _get_total_sign_in_days(ug)
    if day != str(_get_total_sign_in_days(ug) + 1):
        return 11, {'msg': utils.get_msg('gift', 'signin_in_turn')}
    if ug.sign_in_record[day]['has_got']:
        return 11, {'msg': utils.get_msg('gift', 'gift_has_got')}

    if ug.sign_in_record[today].get('today_has_signed_in', False):
        return 11, {'msg': utils.get_msg('gift', 'today_has_signed_in')} 
    # 添加奖励
    awards = game_config.loginbonus_config['sign_in_bonus'].get(month, {}).get(day, {})
    data = tools.add_things(
        rk_user, 
        [{"_id": goods, "num": awards[goods]} for goods in awards if goods],
        where="open_server_gift"
    )
    ug.sign_in_record[day]['has_got'] = True
    #  每天只能签到一次，此字段用来后端判断当天是否已签到过
    ug.sign_in_record[today]['today_has_signed_in'] = True
    ug.do_put()    
    rk_user.user_property.do_put()
    rk_user.user_pack.do_put()
    rk_user.user_cards.do_put()
    rk_user.user_equips.do_put()    
    return 0, data
#pprint(ug.sign_in_record)
pprint(get_sign_in_gift(rk_user, {}))


def show_sign_in_gift(rk_user, params):
    '''
    返回前端当月签到奖励信息
    '''
    now = datetime.datetime.now()
    month = str(now.month)
    #month = '1' 
    today = str(now.day)
    awards = game_config.loginbonus_config['sign_in_bonus'].get(month, {})
    if not awards:
        return 11, {'msg': utils.get_msg('gift', 'no_sign_in_gift')}
    data = {'gifts': {}}
    ug = rk_user.user_gift
    # 当月总签到天数
    sign_in_days = _get_total_sign_in_days(ug)
    # 当月总登陆天数
    month_login_days = rk_user.user_login.month_total_login
    # 新的月份，领取信息全部置False
    if today == '1':
        for n in range(31):
            ug.sign_in_record[str(n)]['has_got'] = False
            ug.sign_in_record[str(n)]['today_has_signed_in'] = False
    for day, award in awards.items():
        data['gifts'].setdefault(day, {})['awards'] = award
        data['gifts'][day]['has_got'] = ug.sign_in_record.setdefault(day, {}).setdefault('has_got', False)
        #if int(day) == sign_in_days+1:
        if int(day) == sign_in_days+1 and not ug.sign_in_record.setdefault(today, {}).setdefault('today_has_signed_in', False):
            data['gifts'][day]['can_get'] = True
        else:
            data['gifts'][day]['can_get'] = False
    ug.do_put()
    data['total_sign_in_days'] = _get_total_sign_in_days(ug)
    data['month_login_days'] = month_login_days
    return 0, data 
pprint(show_sign_in_gift(rk_user, {}))
