#-*- coding: utf-8 -*-
import datetime,traceback,os
import sys
sys.path.insert(0, '/alidata/sites/stg/MaxStrike_prd')
import apps.settings_stg as settings
from django.core.management import setup_environ
setup_environ(settings)



import copy
from apps.models.user_base import UserBase
from apps.models.user_gift import UserGift


from apps.views import main
from apps.oclib import app
from apps.models import data_log_mod
from apps.config import game_config
from apps.common.utils import get_msg

charge_time = "2014-02-14 12:59:59"
uid = "9100214234"
oid = "test_oid_4"
item_id = "com.nega.fenglinhuoshangl.coin07"
charge_way = "re_charge_test"
more_msg = {}

user = UserBase.get(uid)

data = main.charge_api(user, oid, item_id, charge_way=charge_way, more_msg=more_msg)
data_log_mod.set_log('ChargeResultLog',**{'uid':uid,'charge_way':charge_way,\
                                          'result':u"后台补单:" + data['result'],'oid':oid,'item_id':item_id})



def get_charge_award(rk_user, item_id, charge_time):
    """
    充值奖励
    """
    shop_config = copy.deepcopy(game_config.shop_config)
    new_sale = shop_config.get('new_sale',{})
    for key in shop_config:
        if key.endswith('sale'):
            new_sale.update(shop_config.get(key,{}))
    item_info = new_sale[item_id]
    print new_sale

    print item_info
    coin = item_info['num']

    pt_fg = False
    if rk_user.client_type in settings.ANDROID_CLIENT_TYPE and 'charge_award' in game_config.android_config:
        charge_award = game_config.android_config['charge_award']
    else:
        charge_award = shop_config.get('charge_award',{})
    if not charge_award:
        return
    charge_award_info = rk_user.property_info.charge_award_info
    user_gift_obj = UserGift.get_instance(rk_user.uid)
    for gift_id in charge_award:
        gift_conf = charge_award[gift_id]
        start_time = gift_conf.get('start_time')
        end_time = gift_conf.get('end_time','2111-11-11 11:11:11')
        now_str = charge_time # datetime_toString(datetime.datetime.now())
        #未开放或已过期的礼包
        if now_str>end_time or now_str<start_time:
            continue
        
        if gift_id not in charge_award_info:
            charge_award_info[gift_id] = {
                                          'charge_coin':coin,
                                          }
        else:
            #已经领取过的礼包
            if charge_award_info[gift_id].get('has_got',False):
                continue
            charge_award_info[gift_id]['charge_coin'] += coin
        pt_fg = True
        #金额未达到
        if charge_award_info[gift_id]['charge_coin'] < gift_conf.get('charge_coin',0):
            continue
        #满足条件，发奖励
        if gift_conf.get('award',[]):
            charge_award_info[gift_id]['has_got'] = True
            msg = get_msg('charge', 'charge_award') % gift_conf.get('charge_coin',0)
            for award in gift_conf['award']:
                user_gift_obj.add_gift_by_dict(award, msg)

    if pt_fg:
        rk_user.property_info.put()

if charge_time and data['rc'] == 0:
    get_charge_award(user, item_id, charge_time)     

app.pier.save()
