#-*- coding: utf-8 -*-
import datetime,traceback,os
import sys
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)

import time

from apps.models.user_gift import UserGift

uid1150 = {'1100767010': 2300, '1100777178': 2300, '1100775002': 2300, '1100715627': 2300, '1100777288': 1830, '1100771335': 2300, '1100772564': 1150}
uid2310 = {'1100768769': 2600, '1100679685': 3760, '1100716619': 2310, '1100769259': 4950, '1100699903': 5770, '1100774492': 2310, '1100630081': 18510, '1100758266': 8100, '1100540499': 4390, '1100770054': 4620, '1100670255': 2500, '1100768800': 6250, '1100734933': 2350, '1100747296': 2310, '1100508861': 4650, '1100706285': 10410, '1100649285': 16200, '1100755627': 2310, '1100760109': 2310, '1100309953': 26910, '1100757938': 2310, '1100715517': 2310, '1100351444': 2760, '1100771860': 4620}

alluser = []
has_got1 = []
for uid in uid1150:
    alluser.append(uid)
    ug = UserGift.get(uid)
    gift_dict = ug.gift_list
    index_keys = sorted(gift_dict.keys(), reverse=True)
    for key in index_keys:
        if gift_dict[key]['content'].startswith(u'累积充值元宝达到1150奖励'):
            if uid not in has_got1:
                has_got1.append(uid)
            print uid, '1150', gift_dict[key]['content'], gift_dict[key]['award'], time.strftime("%Y%m%d %H:%M:%S", time.localtime(int(gift_dict[key]['upd_time']))), gift_dict[key]['has_got']

print alluser
print list(set(alluser).difference(set(has_got1)))
has_got1 = []
alluser = []
has_got2 = []
for uid in uid2310:
    alluser.append(uid)
    ug = UserGift.get(uid)
    gift_dict = ug.gift_list
    index_keys = sorted(gift_dict.keys(), reverse=True)
    for key in index_keys:
        if gift_dict[key]['content'].startswith(u'累积充值元宝达到1150奖励'):
            if uid not in has_got1:
                has_got1.append(uid)
            print uid, '1150', gift_dict[key]['content'], gift_dict[key]['award'], time.strftime("%Y%m%d %H:%M:%S", time.localtime(int(gift_dict[key]['upd_time']))), gift_dict[key]['has_got']

        if gift_dict[key]['content'].startswith(u'累积充值元宝达到2310奖励'):
         
            if uid not in has_got2:
                has_got2.append(uid)
            print uid, '2310', gift_dict[key]['content'], gift_dict[key]['award'], time.strftime("%Y%m%d %H:%M:%S", time.localtime(int(gift_dict[key]['upd_time']))), gift_dict[key]['has_got']
print alluser
print list(set(alluser).difference(set(has_got2)))
print list(set(has_got2).difference(set(has_got1)))

