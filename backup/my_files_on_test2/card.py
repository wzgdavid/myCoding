# encoding: utf-8
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)


from apps.models.user_gift import UserGift
from apps.models.user_login import UserLogin
from apps.models.user_base import UserBase
from apps.config.game_config import game_config
from apps.models.user_cards import UserCards
from apps.models.user_property import UserProperty
from apps.models.user_dungeon import UserDungeon
from apps.models.user_pack import UserPack
from apps.models.user_property import UserProperty
from apps.models.user_equips import UserEquips
from apps.models.collection import UserCollection
import json
import copy
import datetime
from apps.common.utils import create_gen_id
from apps.common import utils
import time
from apps.models import data_log_mod
from apps.models import GameModel


def set_decks():
    user_card_obj = UserCards.get_instance(UID)
    old_leader_ucid = user_card_obj.leader_ucid
    decks = user_card_obj.deck
    cards = user_card_obj.cards.keys()
    cards_info = user_card_obj.cards_info
    print  'data=',json.dumps(cards,indent=1)



#set_decks()


'''
card
201408151809039998130 {u'lv': 15, u'talent_lv': 1, u'cid': u'69_card', u'exp': 5670, u'upd_time': 1408097343}
'''
def show_all_cards():
    user_card_obj = UserCards.get_instance(uid)
    cards = user_card_obj.cards
    ucids = [ucid for ucid in cards]
    ucids.sort()
    for ucid in ucids:
        print ucid,cards[ucid]
	# del card
        #if cards[ucid]['upd_time'] == 1417750539:
	#    user_card_obj.cards.pop(ucid)
    user_card_obj.do_put()
    print 'cards length', len(cards)

    cards_info = user_card_obj.cards_info
    decks = cards_info['decks']
    pprint(cards) 
#show_all_cards()
'''   result of   show_all_cards()
201408291506056267413 {u'lv': 1, u'talent_lv': 0, u'upd_time': 1409295965, u'exp': 0, u'cid': u'66_card'}
201409090939037535481 {u'lv': 1, u'talent_lv': 0, u'upd_time': 1410226743, u'exp': 1, u'cid': u'3_card'}
201408291506056299841 {u'lv': 4, u'talent_lv': 0, u'upd_time': 1409295965, u'exp': 264, u'cid': u'69_card'}
201409090930405166144 {u'lv': 1, u'talent_lv': 0, u'cid': u'3_card', u'exp': 1, u'upd_time': 1410226240}
201408291506056306713 {u'lv': 1, u'talent_lv': 0, u'upd_time': 1409295965, u'exp': 0, u'cid': u'58_card'}
201408291506056292824 {u'lv': 4, u'talent_lv': 1, u'upd_time': 1409295965, u'exp': 336, u'cid': u'2_card'}
'''
def add_card(cid):
    ucid = create_gen_id()
    #cid = '3_card'
    user_cards_obj = UserCasuser_card_obj = UserCards.get_instance(uid)
    user_cards_obj.cards[ucid] = {
                            'cid':cid,
                            'lv': 1,
                            'exp': 0,
                            'talent_lv':0,
                            'upd_time':int(time.time()),
                            }
    user_cards_obj.do_put()
    
    #UserCollection.get_instance(uid).add_collected_card(cid)

#add_card('3_card')

show_all_cards()

def show_user_cards_fields():
    user_card_obj = UserCards.get_instance(uid)
    print 'user_card_obj.cards','-'*50
    pprint (user_card_obj.cards)
    print 'user_card_obj.cards_info','-'*50
    #pprint (user_card_obj.cards_info)
    print 'user_card_obj.decks','-'*50
    #pprint (user_card_obj.decks)    
#show_user_cards_fields()

