#-*- coding: utf-8 -*-
import datetime,traceback,os
import sys
sys.path.insert(0, '/data/sites/stg/qz')
import apps.settings_stg as settings
from django.core.management import setup_environ
setup_environ(settings)

from apps.common.utils import get_msg

import copy

#from apps.config import game_config
from apps.config.game_config import game_config

#game_config.set_subarea('1')

def main():
    f = open('city_config.txt','w')
    game_config.set_subarea('1')
    material_config = game_config.material_config
    for mat in material_config:
        print material_config[mat]
        material_config[mat]['test'] = 0
        f.write(mat+'\n')
    f.close()
    material_config.put()
if __name__ == "__main__":
    main()
