#-*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/data/sites/MaxStrike')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)
from apps.models.user_base import UserBase
from apps.models.charge_record import ChargeRecord
from apps.common.utils import datetime_toString
import datetime
oid='12999763169054705758.1339156342973080'
uid='2100237082'
item_id = 'com.nega.fenglinhuoshangl.coin05'
item_num =2310
item_price =198
charge_way='googleplay'
rk_user = UserBase.get(uid)
before_coin = rk_user.property_info.coin

if rk_user.property_info.property_info['first_charge']:
    rk_user.property_info.property_info['coin'] += item_num * 2
else:
    rk_user.property_info.property_info['coin'] += item_num

after_coin = rk_user.property_info.property_info['coin']
record_data = {
"oid":oid,
"uid":uid,
"platform":rk_user.platform,
"lv":rk_user.property_info.lv,
"price":item_price,
"item_id":item_id,
"item_num":item_num,
"createtime":datetime_toString(datetime.datetime.now()),
"before_coin":before_coin,
"after_coin":after_coin,
"client_type":rk_user.client_type,
"charge_way":charge_way,
}
#ChargeRecord.set_record(**record_data)
#rk_user.property_info.property_info['first_charge'] = False
#rk_user.property_info.do_put()
