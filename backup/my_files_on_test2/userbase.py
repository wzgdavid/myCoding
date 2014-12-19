# encoding: utf-8
import sys
sys.path.insert(0, '/alidata/sites/stg/qz/')
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)


from apps.models.user_base import UserBase
from apps.config.game_config import game_config
from common import uid, pprint

game_config.subareas_conf()
game_config.set_subarea('1')
ub = UserBase.get(uid)

def show_baseinfo():
    userbase = UserBase.get(uid)
    pprint (userbase.baseinfo)
    print len(userbase.baseinfo['received_mails'])
    #print userbase.uid
    #print userbase.user_cards
show_baseinfo()

def clear_received_mail():
    ub.baseinfo['received_mails'] = []
    del ub.baseinfo['received_mails']
    ub.do_put()
#clear_received_mail()

def test_recover_bug():
    '''
    10-24
    '''
    userbase = UserBase.get(uid)
    print userbase.wrapper_info()
#test_recover_bug()

def username():
    ub.set_name('sss')
    ub.do_put()
    print ub.username    
#username()
