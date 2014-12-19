#-*- coding: utf-8 -*-
import importlib
import datetime,traceback,os
import ast
import sys
sys.path.insert(0, '/data/sites/stg/qz')
import apps.settings_stg as settings
from django.core.management import setup_environ
setup_environ(settings)

from apps.models.user_souls import UserSouls
from apps.models.user_equips import UserEquips
from apps.config.game_config import game_config
game_config.set_subarea('1')
def main():
    uid = str(sys.argv[1])
    ue = UserEquips.get_instance(uid)
    for eid in game_config.equip_config:
            ue.add_equip(eid,where='miao')
    ue.do_put()

if __name__ == '__main__':
    main()

