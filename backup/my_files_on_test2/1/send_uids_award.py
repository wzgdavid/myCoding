#-*- coding: utf-8 -*-
"""
若没有参数  则为测试
否则 参数为dev表示正式
"""
import datetime,traceback,os
import sys
sys.path.insert(0, '/data/sites/MaxStrikecn')
import apps.settings as settings
from django.core.management import setup_environ
setup_environ(settings)

from apps.common.utils import get_msg
from apps.models.user_gift import UserGift


#msg = u"qa_add"
#msg = u"百度贴吧推荐奖励"
#msg = u"风林火山之我型我秀"
msg = u"内部奖励"
#msg = u"微信活动"
#msg = u"加藤鹰战袍奖励"
#msg = u"“你提我改”奖励"

staff_str = '''
1100762034
'''
#sendid = '1100469219'

staff = staff_str.split(os.linesep)
#staff.append('1100469219')

###0-攻击型，1-防御型，2-血型，3-回复型，4-平衡
safe_list = []
for uid in staff:
    uid = uid.strip()
    user_gift_obj = UserGift.get(uid)
    print uid
	
    if not uid.startswith('1'):
        continue
    gift = [#奖励内容
        {'coin': 4000},
        #{'stone': 2000000},
        #{'200_card':{'lv':1,'num':50}},
        #{'239_card':{'lv':1,'category':'2','num':1}},
        #{'239_card':{'lv':1,'category':'4','num':1}},
        #{'239_card':{'lv':1,'num':1}},
    ]
        #{'223_card': {'category': '2', 'num': 1}},
    for item in gift:
        print item ,'send gift'
    for award in gift:
        user_gift_obj.add_gift_by_dict(award, msg)

    if len(sys.argv) == 2 and  sys.argv[1] == 'dev': 
        safe_list.append(user_gift_obj)
        #user_gift_obj.do_put()
        print "just test"
        pass
    elif len(sys.argv) == 1:
        safe_list.append(user_gift_obj)
        #user_gift_obj.do_put()
        print 'send obj'
        pass
print '\n\n'
print msg
print gift
if raw_input("are you sure to send this gifts?   ") != 'yes':
    print "cancel give gift"
else:
    for ug in safe_list:
        print ug.uid, gift
        ug.do_put()
        pass
    print "had sended!"
