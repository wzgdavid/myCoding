#-*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/data/sites/stg/qz/')
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)

import copy
from apps.common import utils
from apps.models.user_gift import UserGift
from apps.models.user_login import UserLogin
from apps.models.user_base import UserBase
from apps.config.game_config import game_config
from apps.models.user_property import UserProperty
from apps.models.user_equips import UserEquips
from apps.models.user_cards import UserCards
from apps.models.user_souls import UserSouls
from apps.models.user_pack import UserPack
import json

UID = '9100213902'


def buy_vip_gift():
    '''
    购买vip礼品包
    '''
   #gift_id = params.get('vip_gift_id','0')
    vip_gift_id = '2'
 
    user_property_obj = UserProperty.get(UID)
    user_pack_obj = UserPack.get_instance(UID)
    user_equips_obj = UserEquips.get_instance(UID)
    user_card_obj = UserCards.get_instance(UID)
    user_soul_obj = UserSouls.get_instance(UID)
    vip_cur_level = user_property_obj.vip_cur_level
    print vip_cur_level
    vip_charge_info = user_property_obj.property_info['vip_charge_info']
    print user_property_obj.property_info['vip_charge_info']
    vip_gift_sale_config = game_config.shop_config.get('vip_gift_sale',{})
    #判断vip礼包id是否有效
    if not vip_gift_id:
           return 11,{'msg':utils.get_msg('gift','invalid_gift')}
    #判断是否存在该vip礼包
    if vip_gift_id not in vip_gift_sale_config:
           return 11,{'msg':utils.get_msg('gift','git_not_exist')}
    #判断玩家的vip等级是否达到
    if vip_cur_level not in [i for i in range(int(vip_cur_level) + 1)] or int(vip_gift_id) > vip_cur_level:
           return 11,{'msg':utils.get_msg('gift','level_not_enough')}
    #判断玩家是否已经购买相应的vip礼包
    if vip_gift_id in vip_charge_info:
           return 11,{'msg':utils.get_msg('gift','gift_already_buy')}
    else:
         data = {}
         coin = vip_gift_sale_config[vip_gift_id]['coin']
         user_cur_coin = user_property_obj.coin
        #判断玩家的元宝是否达到
         if not user_property_obj.is_coin_enough(coin):   
                return 11,{'msg':utils.get_msg('gift','coin_not_enough')}
         else:       
                user_property_obj.minus_coin(coin) #扣除元宝               
                gift = vip_gift_sale_config[vip_gift_id]['gift']
                for val in gift:
                       explode = val[0].split('_')
                       #物品的类别
                       category = val[0]
                       #物品的数量  
                       num = val[1]
                       #添加药水
                       if 'item' in explode:
                              if explode[1] not in data:
                                    data[explode[1]] = {}
                              data[explode[1]][category] = num
                              user_pack_obj.add_item(category,num)                                           
                       #添加材料
                       elif 'mat' in explode:
                              if 'material' not in data:
                                    data['material'] = {}
                              data['material'][category] = num
                              user_pack_obj.add_material(category,num)                                                                                
                       #添加道具
                       elif 'props' in explode:
                              if explode[1] not in data:
                                    data[explode[1]] = {}
                              data[explode[1]][category] = num
                              user_pack_obj.add_props(category,num)
                       #添加装备
                       elif 'equip' in explode and len(explode) == 2:
                              if explode[1] not in data:
                                    data[explode[1]] = {}
                              data[explode[1]][category] = num
                              user_equips_obj.add_equip(category,num)                   
                       #添加碎片
                       elif 'soul' in explode:
                              if explode[2] not in data:
                                     data[explode[2]] = {}
                              #添加武将碎片
                              if 'card' in explode:
                                     if explode[1] not in data[explode[2]]:
                                             data[explode[2]][explode[1]] = {}
                                     category = explode[0]+'_'+explode[1]
                                     user_soul_obj.add_normal_soul(category,num) 
                                     data[explode[2]][explode[1]][category] = num                
                              #添加装备碎片
                              if 'equip' in explode:
                                     if explode[1] not in data[explode[2]]:
                                             data[explode[2]][explode[1]] = {}
                                     count = len(explode)
                                     if count == 3:category = explode[0]+'_'+explode[1]
                                     if count == 4:category = explode[0]+'_'+explode[1]+'_'+explode[3]
                                     user_soul_obj.add_equip_soul(category,num,None)
                                     data[explode[2]][explode[1]][category] = num    
                       elif 'card' in explode and len(explode) == 2:
                              if explode[1] not in data:
                                     data[explode[1]] = {}
                              data[explode[1]][category] = num
                              user_card_obj.add_card(category,num)
               #把已购买的vip礼包id添加到vip_charge_info列表中
                user_property_obj.add_vip_gift_id(vip_gift_id)
                print user_property_obj.property_info['vip_charge_info']
    k = json.dumps(data,indent=1)
    print 'data=',k

buy_vip_gift()
