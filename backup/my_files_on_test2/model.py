# encoding: utf-8
from common import uid, qz_path
import sys
sys.path.insert(0, qz_path)
import bisect
import copy
import datetime
import random

import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

from apps.common import utils
from apps.config.game_config import game_config
from apps.models import GameModel, pvp_redis
from apps.models.pvp_redis import get_pvp_redis
from apps.models.user_base import UserBase
from apps.models.user_cards import UserCards
from apps.models.user_equips import UserEquips
from apps.models.user_gift import UserGift
from apps.models.user_mail import UserMail
from apps.models.user_marquee import UserMarquee
from apps.models.user_pack import UserPack
from apps.models.user_pk_store import UserPKStore
from apps.models.user_property import UserProperty
from apps.models.user_real_pvp import UserRealPvp
from apps.models.user_souls import UserSouls
from apps.oclib import app
from apps.oclib.model import BaseModel, UserModel
from apps.realtime_pvp import readying_player_redis



# from apps.models.user_property import UserProperty
# from apps.models.friend import Friend

def look_model():
    upk = UserPKStore.get_instance(uid)
    print upk.user_property, upk.game_config
    #print upk.user_cards, upk.user_mystery_store, upk.user_login
    print UserPKStore._ALL_USER_CLASSES
look_model()

