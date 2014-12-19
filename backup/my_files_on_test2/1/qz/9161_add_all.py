#-*- coding: utf-8 -*-
import importlib
import datetime,traceback,os
import ast
import sys
sys.path.insert(0, '/data/sites/op/qz')
import apps.settings_stg as settings
from django.core.management import setup_environ
setup_environ(settings)

from apps.models.user_souls import UserSouls
from apps.models.user_equips import UserEquips
from apps.models.user_dungeon import UserDungeon
from apps.models.user_cards import UserCards
from apps.models.user_pack import UserPack
from apps.models.user_property import UserProperty 
from apps.config.game_config import game_config
game_config.set_subarea('1')
def main():
    uid = str(sys.argv[1])
    ue = UserEquips.get_instance(uid)
    for eid in game_config.equip_config:
        ue.add_equip(eid,where='miao')
    ue.do_put()
    up = UserPack.get_instance(uid)
    for mat_id in game_config.material_config:
        up.add_material(mat_id,100,where='miao')

    for item_id in game_config.item_config:
        up.add_item(item_id,100,where='miao')

    for props_id in game_config.props_config:
        up.add_props(props_id,1000,where='miao')

    up.do_put()
    us = UserSouls.get_instance(uid)
    for eid in game_config.equip_config:
        if game_config.equip_config[eid].get('need_souls',''):
            us.add_equip_soul(eid,100,where='miao')
            #print eid
        else:
            parts = game_config.equip_config[eid].get('need_soul_types_num',0)
            #print eid, parts
            for i in xrange(1,parts+1):
                us.add_equip_soul(eid+'_'+str(i),100,where='miao')
    uc = UserCards.get_instance(uid)
    for card_id in game_config.card_config:
        uc.add_card(card_id,lv=1,where='miao')
        us.add_normal_soul(card_id,10,where='miao')
    us.do_put()

    upr = UserProperty.get_instance(uid)
    upr.add_exp(15000000)
    upr.add_coin(5000000)
    upr.add_gold(100000000)
    upr.add_card_exp_point(10000000)
    upr.do_put(

    ud = UserDungeon.get(uid)
    ud.normal_current['floor_id'] = '22'
    ud.do_put()
if __name__ == '__main__':
    main()

