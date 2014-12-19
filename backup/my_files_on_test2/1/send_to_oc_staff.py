#-*- coding: utf-8 -*-
###0-攻击型，1-防御型，2-血型，3-回复型，4-平衡
import sys
import os
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)


from apps.models.user_gift import UserGift


# msg = get_msg('charge','charge_award')
msg = u"内部福利"

staff = ['1100709023']
#staff = ['1100268619']  # my id
staff = ['1100469219']
staff = '''
1100213358
'''
staff = staff.split(os.linesep)
for uid in staff:
    uid = uid.strip()
    if not uid or not uid.startswith("1"):
        continue
    user_gift_obj = UserGift.get(uid)
    print uid
    if uid in '''1100215519
        1100234370
        1100469219
        ''':
        gift = [#奖励内容
            {'285_card':{'lv':1,'category':'2','num':2}},
            #{'coin':3000},
            #{'gold':1000000},
        ]

    elif uid in '''1100213678
1100216783
1100213582 ''':
        gift = [#奖励内容
            #{'170_card':{'lv':1,'category':'2','num':3}},
            {'270_card':{'lv':1,'category':'0','num':1}},
            #{'4_equip':{'num':5}},
            {'coin':3000},
        ]

    elif uid in '''1100752809
1100213787''':
        gift = [#奖励内容
            #{'170_card':{'lv':1,'category':'2','num':1}},
            {'282_card':{'lv':1,'num':1,'category':'0'}},
            #{'4_equip':{'num':5}},
            {'coin':3000},
        ]


    else:
        gift = [#奖励内容
                #{'36_equip':{'num':3}},
                {'285_card':{'lv':1,'num':1,'category':'2'}},
                {'282_card':{'lv':1,'num':1},'category':'2'},
                #{'49_equip':{'lv':1,'num':1}},
                #{'223_card':{'lv':1,'num':1,'category':'2'}},
                #{'gold':100000},
                {'coin':3000},
        ]



    for award in gift:
        print award
        user_gift_obj.add_gift_by_dict(award, msg)
    user_gift_obj.do_put()


