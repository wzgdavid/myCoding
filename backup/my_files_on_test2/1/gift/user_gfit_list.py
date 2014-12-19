#-*- coding: utf-8 -*-
import datetime,traceback,os
import sys
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)

import time

from apps.models.user_gift import UserGift

uid = sys.argv[1]
ug = UserGift.get(uid)
gift_dict = ug.gift_list
print gift_dict.keys()
index_keys = sorted(gift_dict.keys(), reverse=True)
for key in index_keys:
    print gift_dict[key]['content'],gift_dict[key]['award'], time.strftime("%Y%m%d %H:%M:%S", time.localtime(int(gift_dict[key]['upd_time']))), gift_dict[key]['has_got'] 
