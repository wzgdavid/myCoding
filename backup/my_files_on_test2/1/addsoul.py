#-*- coding: utf-8 -*-
import datetime,traceback,os
import sys
sys.path.insert(0, '/data/sites/MaxStrike')
from django.core.management import setup_environ
import apps.settings as settings
setup_environ(settings)


import copy
from apps.models.user_souls import UserSoul

from apps.views import main
from apps.oclib import app
from apps.models import data_log_mod
from apps.config import game_config

def main():
    findlist = [[2100225843,8],[2100227898,13],[2100234249,1],[2100235646,1]\
        ,[2100237237,4],[2100242679,1],[2100246621,1],[2100255602,1]\
        ,[2100282460,1],[2100314957,1],[2100356915,1],[2100362456,0]\
        ,[2100386599,1],[2100409004,1],[2100413721,1],[2100433241,1]\
        ,[2100444907,1],[2100450596,3],[2100456502,1],[2100457749,1]\
        ,[2100494067,2],[2100499712,1],[2100501052,4],[2100505929,3]\
        ,[2100516713,3],[2100529919,1],[2100533119,1],[2100533183,1]]
    for flist in findlist:
        #us = UserSoul.get_instance(flist[0])
        #print us.get_super_soul_num
        #us.add_super_soul(flist[1])
        print flist[0],flist[1]
if __name__ == "__main__":
    main()

