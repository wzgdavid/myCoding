# encoding: utf-8
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

import bisect
import random
import datetime
from apps.common import utils
from apps.models.user_real_pvp import UserRealPvp
from apps.models.user_base import UserBase
from apps.models.user_login import UserLogin
# from apps.models.friend import Friend
from apps.models import pvp_redis
from apps.oclib import app
from apps.models.user_mail import UserMail
from apps.realtime_pvp import readying_player_redis
from apps.config.game_config import game_config
from apps.models.pvp_redis import get_pvp_redis
from apps.models.user_property import UserProperty
from apps.models.user_mail import UserMail
from apps.models.user_gift import UserGift
from apps.common import tools
game_config.subareas_conf()
game_config.set_subarea('1')
sid = 'system_%s' % (utils.create_gen_id())
user_mail = UserMail.hget(uid, sid)
rk_user = UserBase.get(uid)


def show_all_mails():
    all_mail = UserMail.hgetall(uid)
    #for mail_id, mail_info in all_info.items():
    #    print mail_id, '------', mail_info

    pprint(all_mail)   
#show_all_mails()


def modify_one_mail():
    all_mail = UserMail.hgetall(uid)
    #print all_mail
    for key in all_mail:
    
        if key == 'system_201411111104385687940':
            all_mail[key]['open_time'] = '1234'
            this_mail = UserMail.hget(uid, key)
            this_mail.hput()
            print this_mail
    key == 'system_201411111104385687940'
    this_mail = UserMail.hget(uid, key)
    print this_mail.mail_info
    this_mail.mail_info['read_time']= '123'
    this_mail.hput()
#modify_one_mail()

def delete_all_mails():
    all_info = UserMail.hgetall(uid)
    #for mail_id, mail_info in all_info.items()[:-3]:# 注意 这里不是去全删
    for mail_id, mail_info in all_info.items():
        print mail_id, mail_info
        umobj = UserMail.hget(uid, mail_id)
        umobj.delete()

#delete_all_mails()


def send_a_mail():
    sid = 'system_%s' % (utils.create_gen_id())
    user_mail_obj = UserMail.hget(uid, sid)

    #awards = {'coin': 50, 'gold': 50, 'honor':500}
    awards = {}
    #user_mail_obj.set_awards_description(awards)
    user_mail_obj.set_mail(mailtype='system', title='eee', content='人工e邮件',award=awards)
    #user_mail_obj.set_mail(type='system',content='mail pvp')
    user_mail_obj.hput()

#send_a_mail()


def send_mails(data):
    if True:
        if 'honor_award' in data:
            content = data['honor_award']['content']
            award = data['honor_award']['award']
            sid = 'system_%s' % (utils.create_gen_id())
            user_mail = UserMail.hget(uid, sid)
            user_mail.set_awards_description(award)
            user_mail.set_mail(mailtype='system', content=content, award=award)
data = {'honor_award': {'content': u'\u529f\u52cb\u5956\u52b1', 'award': {'honor': 2250}}}
#send_mails(data)



def send_op_mail(rk_user):
    '''
    发运营邮件
    判断运营是否有新配邮件,这里邮件特指mail_config['mail_list']里的邮件,需要一些实时性，非一些登陆奖励类邮件
    '''
    mail_list = game_config.mail_config.get('mail_list')
    if not mail_list:
        return
    for mail in mail_list:
        mid = mail['mail_id']
        if not rk_user.baseinfo.get('received_mails'):
            rk_user.baseinfo['received_mails'] = []
            rk_user.put()
        received_mails = rk_user.baseinfo['received_mails']
        # 没收过这封邮件,并且邮件在时间段内，发邮件
        if mid not in received_mails:
            if _is_between_times(mail):
                sid = 'system_%s' % (utils.create_gen_id())
                mailtype = 'system_qa'
                title = mail['title']
                content = mail['content']
                award = mail['award']
                user_mail_obj = UserMail.hget(rk_user.uid, sid)
                user_mail_obj.set_mail(mailtype=mailtype, title=title, content=content, award=award)

                received_mails.append(mid)
                # 去掉时间太久的不必要的邮件
                if len(received_mails) > 30:
                    received_mails.pop(0)
                rk_user.put()

def _is_between_times(mail):
    if len(mail['start_time']) == len(mail['end_time']) == 19:
        now = utils.datetime_toString(datetime.datetime.now())
        if mail['start_time'] <= now <= mail['end_time']:
            return True
    return False


#send_op_mail(rk_user)

def show_mails(rk_user, params):
    """
    获取邮件列表
    'type': 'system': 系统邮件
    'type': 'pvp'   : pvp邮件 
    Returns:
        {'show_mails': 
            {1: {'awards': [
                    {'equipSoul': {'equip_type': u'1', 'good_id': u'53003_equip', 'num': 1}},                
                    {'mat': {'good_id': u'3_mat', 'num': 2}},
                    {'gold': {'good_id': u'gold', 'num': 10}},
                    {'props': {'good_id': u'1_props', 'num': 1}},
                    {'equip': {'color': u'green', 'good_id': u'13001_equip', 'num': 3}},
                    {'cardSoul': {'good_id': u'5_card', 'num': 1}},
                    {'fight_soul': {'good_id': u'fight_soul', 'num': 100}},
                    {'card': {'good_id': u'5_card', 'num': 1}},
                    {'honor': {'good_id': u'honor', 'num': 100}},
                    {'equipSoul': {'good_id': u'12002_equip', 'num': 1}}
                ],
                'can_get': True,
                'content': u'5345',
                'create_time': u'2014-11-04 11:32:56',
                'mid': u'201411041132562390414',
                'type': u'system'},
            2:  ......
    """
    data = {}
    all_info = UserMail.hgetall(rk_user.uid)
    expire_days = game_config.mail_config.get('expire_days', 2)
    clear_date = (datetime.datetime.now() - datetime.timedelta(days=expire_days)).strftime('%Y-%m-%d %H:%M:%S')
    # 根据创建时间排序
    key_create_time_list = [(m, all_info[m]['mail_info'].get('create_time', ''), 
                            all_info[m]['mail_info'].get('open_time')) for m in all_info]

    key_create_time_list = sorted(key_create_time_list , key=lambda key_time: key_time[1], reverse=True)
    for index, key_create_time in enumerate(key_create_time_list):
        key, create_time, open_time = key_create_time
        mail_info = all_info[key]['mail_info']
        can_get = mail_info.get('can_get', False)
        print 'create time:', create_time,  'open time:',open_time,  ' can get:', can_get
        if can_get is False and clear_date > open_time:
        #if can_get is False:
            umobj = UserMail.hget(rk_user.uid, key)
            umobj.delete()
            continue

        this_data = {
            'type': mail_info['type'],
            'title': mail_info['title'],
            'content': mail_info['content'],
            'can_get': mail_info['can_get'],
            'awards': [tools.pack_good(good, num) for good, num in mail_info['awards'].items()],
            'create_time': mail_info['create_time'],
            #'mid': mail_info['mid'],
            'mid': key,
        }
        data[index + 1] = this_data
    #print data
    return {'show_mails': data}

#show_mails = show_mails(rk_user, {})['show_mails']
#temp_mails =  show_mails.values()
#pprint (temp_mails)

def test_is_between_times():
    mail = {
        'mail_id': '2014-11-07-18',
        'title': unicode('18','utf-8'),   # 邮件标题
        'content': unicode('test2df','utf-8'),  # 正文
        'start_time': '2014-10-06  10:00:00',  #开始时间
        'end_time': '2014-12-15  15:00:00',   #结束时间
        'award': {},
    }
    try:
        start_time = utils.string_toDatetime(mail['start_time'])
        end_time = utils.string_toDatetime(mail['end_time'])
    except ValueError:
        print 'start or end time config error'
        return False
    now = datetime.datetime.now()
    if start_time <= now <= end_time:
        return True
    else:
        return False

print test_is_between_times()
