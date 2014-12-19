#-*- coding: utf-8 -*-
import importlib
import datetime,traceback,os
import ast
import sys
sys.path.insert(0, '/data/sites/stg/qz')
import apps.settings_stg as settings
from django.core.management import setup_environ
setup_environ(settings)

from apps.config.game_config import game_config
game_config.set_subarea('1')
def main():
    dungeon_config = game_config.dungeon_config
    drop_config = game_config.drop_info_config['normal_dungeon']
    drop_mat = drop_config.keys()
    drop_soul = drop_config['soul'].keys()
    for floor_id in dungeon_config:
        floor_info = dungeon_config[floor_id]['rooms']
        for room_id in floor_info:
            v_drop = floor_info[room_id].get('drop_info',{})
            iv_drop = floor_info[room_id].get('invisible_drop',{})
            for drop_type in v_drop:
                all_drop = v_drop[drop_type]
                if drop_type == 'soul':
                    check_info = drop_soul
                else:
                    check_info = drop_mat
                for drop in all_drop:
                    if drop not in check_info:
                        print 'visible_drop', floor_id,room_id,drop_type,drop   
            for drop_type in iv_drop:
                all_drop = iv_drop[drop_type]
                if drop_type == 'soul':
                    check_info = drop_soul
                else:
                    check_info = drop_mat
                for drop in all_drop:
                    if drop not in check_info:
                        print 'invisible_drop', floor_id,room_id,drop_type,drop
if __name__ == '__main__':
    main()

