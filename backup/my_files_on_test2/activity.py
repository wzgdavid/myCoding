# encoding: utf-8
from common import uid, qz_path
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)
import time
import datetime
from apps.common import utils
from apps.models.user_gift import UserGift
from apps.models.user_login import UserLogin
from apps.models.user_base import UserBase
from apps.config.game_config import game_config
from apps.models.user_cards import UserCards
from apps.models.user_property import UserProperty
from apps.models.user_dungeon import UserDungeon
from apps.models.user_pack import UserPack
from apps.models.user_equips import UserEquips
from apps.models.user_activity import UserActivity
import json
#uid = '9100214727'
game_config.subareas_conf()
game_config.set_subarea('1')
def show_banquet_info():
    game_config.subareas_conf()
    game_config.set_subarea('1')
    open_gaps = game_config.operat_config.get('open_stamina_banquet_gaps')
    ul = UserLogin.get_instance(uid)
    user_banquet_info = ul.banquet_info
    print user_banquet_info


#show_banquet_info()



def get_banquet_stamina():
    """
    开始宴席
    params:
        click_num:  玩家点击次数，据此来算玩家回体数
    """
    open_time_gaps = game_config.operat_config.get('open_stamina_banquet_gaps', [])
    now = datetime.datetime.now()
    now_date_day = now.strftime('%Y-%m-%d')
    now_hour_min = now.strftime('%H:%M')
    this_time_gap = utils.between_gap(now_hour_min, open_time_gaps)
    if not this_time_gap:
        return 11,{'msg':utils.get_msg('active', 'not_in_time')}
    #获取时间区间的最小值
    time_start = '%s %s:00'%(now_date_day,str(this_time_gap[0]))
    start_time = utils.string_toTimestamp(time_start)
    #查询是否已经领取体力
    ul = UserLogin.get_instance(uid)
    ul.banquet_info[str(start_time)] = False
    ul.do_put()
    banquet_info = ul.banquet_info
    if banquet_info.get(str(start_time), False):
        return 11, {'msg':utils.get_msg('active', 'already_banquet')}
    #根据点击次数获取可以领取多少体力
    click_num = 30
    click_num_awards_conf = game_config.operat_config.get('banquet_click_num_awards', {})
    suitable_gap = utils.between_gap(click_num, click_num_awards_conf)
    get_stamina = click_num_awards_conf.get(suitable_gap, 0)
    user_property = UserProperty.get_instance(uid)   
    user_property.add_stamina(get_stamina)
    print get_stamina
    return {'add_stamina': get_stamina}
print get_banquet_stamina()


def show_user_activity_fields():
    user_activity_obj = UserActivity.get_instance(uid)
    print 'user_activity_obj.explore', user_activity_obj.explore
    print 'user_activity_obj.banquet', user_activity_obj.banquet
#show_user_activity_fields()




def look_diff():
    now = datetime.datetime.now()
    now_date_day = now.strftime('%Y-%m-%d')
    now_hour_min = now.strftime('%H:%M')
    time_start = '%s %s:00'%(now_date_day,'10:00')
    time_end = '%s %s:00'%(now_date_day,'15:00')

    start_time =datetime.datetime.strptime(time_start,'%Y-%m-%d %H:%M:%S')
    end_time =datetime.datetime.strptime(time_end,'%Y-%m-%d %H:%M:%S')
    start_time = int(time.mktime(start_time.timetuple()))
    end_time = int(time.mktime(end_time.timetuple()))

    print start_time, end_time
    print '*'*100

    start_time = utils.string_toTimestamp(time_start)
    end_time = utils.string_toTimestamp(time_end)

    
    print start_time, end_time
#look_diff()
