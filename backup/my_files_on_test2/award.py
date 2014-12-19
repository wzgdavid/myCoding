# encoding: utf-8
import sys
sys.path.insert(0, '/data/sites/stg/qz/')
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

import bisect
import random
import datetime
from apps.common import utils
from apps.models.user_real_pvp import UserRealPvp
from apps.models.user_base import UserBase
# from apps.models.user_property import UserProperty
# from apps.models.friend import Friend
from apps.models import pvp_redis
from apps.oclib import app
from apps.models.user_mail import UserMail
from apps.realtime_pvp import readying_player_redis
from apps.config.game_config import game_config
from apps.models.pvp_redis import get_pvp_redis
from apps.models.user_property import UserProperty
from apps.models.user_gift import UserGift
from common import uid
game_config.subareas_conf()
game_config.set_subarea('1')
sid = 'system_%s' % (utils.create_gen_id())
user_mail = UserMail.hget(uid, sid)

def get_self_rank():
    user_real_pvp_obj = UserRealPvp.get_instance(uid)  
    print user_real_pvp_obj.pvp_rank()
    print user_real_pvp_obj.yesterday_pvp_rank()

#get_self_rank()


def test_mail():
    sid = 'system_%s' % (utils.create_gen_id())
    user_mail_obj = UserMail.hget(uid, sid)
    
    awards = {'coin': 50}
    #user_mail_obj.set_mail(mailtype='system',content='test mail',award=awards,awards_description='test mail desc')
    #user_mail_obj.set_mail(type='system',content='mail pvp')
    #user_mail_obj.hput()

#test_mail()




def give_award(award,where=None):
    up = UserProperty.get_instance(uid)
    user_real_pvp = UserRealPvp.get(uid)
    if True:

        tmp = {}
        for key in award:
            if key == 'gold':
                up.add_gold(award[key],'award_%s' % where)
		up.do_put()
                tmp[key] = award[key]
            elif key == 'coin':
               up.add_coin(award[key],'award_%s' % where)
               tmp[key] = award[key]
            elif key == 'honor':
                user_real_pvp.add_honor(award[key])
		user_real_pvp.do_put()
                tmp[key] = award[key]
        return tmp
def show_self_honor():
    user_real_pvp = UserRealPvp.get(uid)
    print 'self honor', user_real_pvp.honor
    
#print give_award({'gold':12,'honor':20})
#show_self_honor()


def send_mail_and_add_gift(data):
    if 'honor_award' in data:
        sid = 'system_%s' % (utils.create_gen_id())
        user_mail = UserMail.hget(uid, sid)
        user_gift_obj = UserGift.get_instance(uid)
        content = data['honor_award']['content']
        award = data['honor_award']['award']
	award['gift_id'] = user_gift_obj.add_gift(award,content)
	print award['gift_id']
        user_gift_obj.do_put()
        user_mail.set_awards_description(award)
        user_mail.set_mail(mailtype='system', content=content, award=award)

data = {'honor_award':{'content':'test award content', 'award':{'honor': 1}}}
#send_mail_and_add_gift(data)


