#-*- coding: utf-8 -*-
from common import uid, qz_path, pprint
import sys
sys.path.insert(0, qz_path)
import apps.settings_stg as settings_stg
from django.core.management import setup_environ
setup_environ(settings_stg)


import copy
import json
from apps.models.user_mystery_store import UserMysteryStore
from apps.models.user_property import UserProperty
from apps.common import utils
from apps.config.game_config import game_config
from apps.logics import vip
from apps.models import data_log_mod
from apps.models.user_cards import UserCards
from apps.models.user_equips import UserEquips
from apps.models.user_pack import UserPack
from apps.logics import card
from apps.logics import equip
from apps.models.user_base import UserBase
game_config.subareas_conf()
game_config.set_subarea('1')
rk_user = UserBase.get(uid)

def check_card_in_deck(user_card_obj,card_list):
    """
    检查武将是否在队伍中
    """
    game_config.subareas_conf()
    game_config.set_subarea('1')
    for ucid in card_list:
        for deck in user_card_obj.decks:
            ucid_ls = [card['ucid'] for card in deck if card.get('ucid','')]
            if ucid in ucid_ls:
                return 11,utils.get_msg('card','in_deck')
    return 0,''

def equip_stove():
    """
    炼化
    """
    sell_ueids ='201410201603035844619' 
    #卖出的装备为空的时候的处理
    if not sell_ueids:
        return 11,{'msg':utils.get_msg('equip','no_equip')}
    #获取装备的列表
    sell_ueids = sell_ueids.split(',')
    #装备列表去空
    sell_ueids = utils.remove_null(sell_ueids)
    #这里执行两次的原因是防止前台传递过来的是 ,,
    if not sell_ueids:
        return 11,{'msg':utils.get_msg('equip','no_equip')}
    #获取用户装备对象
    user_equip_obj = UserEquips.get_instance(uid)
    user_equips = user_equip_obj.equips
    #循环要卖出的装备 判断是否可以卖出
    for sell_ueid in sell_ueids:
        #检查装备是否存在
        if sell_ueid not in user_equips:
            return 11,{'msg':utils.get_msg('equip','no_equip')}
        #检查装备是否装备武将
        try:
            sell_ueid_bind = user_equips[sell_ueid]['used_by']
        except:
            sell_ueid_bind = ''
        #判断装备是否已经装备在武将身上
        if sell_ueid_bind:
            return 11,{'msg':utils.get_msg('equip','is_used')}
    #计算卖出获得的铜钱数量
    #get_gold = 0
    #获取用户的装备的eid和等级
    sell_eids_info = [user_equip_obj.get_equip_dict(ueid) for ueid in sell_ueids]
    #treasure_sell_gold = game_config.equip_exp_conf['treasure_sell_gold']
    #common_base_gold = game_config.equip_exp_conf['common_base_gold']
    return 0,{'equips_info':sell_eids_info,'equips_ueids':sell_ueids}
#print equip_stove()

def card_stove():
    """
    炼化
    """
    game_config.subareas_conf()
    game_config.set_subarea('1')
    #sell_ucids = params['sell_ucids']
    user_property_obj = UserProperty.get_instance(uid)
    sell_ucids = '201410161423224907513'
    if not sell_ucids:
        return 11,{'msg':utils.get_msg('card','no_cost_card')}
    sell_ucids = sell_ucids.split(',')
    sell_ucids = utils.remove_null(sell_ucids)
    user_card_obj = UserCards.get(uid)
    #检查武将是否存在
    for ucid in sell_ucids:
        if ucid and not user_card_obj.has_card(ucid):
            return 11,{'msg':utils.get_msg('card','no_card')}
    #如果有主角卡，则不能消耗
    if user_property_obj.leader_role_card in sell_ucids:
        return 11,{'msg':utils.get_msg('card','role_card')}
    #带装备武将不允许卖出
    if user_card_obj.is_equip_used(sell_ucids):
        return 11,{'msg':utils.get_msg('equip','is_used')}
    #被锁定武将不能卖出
    if user_card_obj.is_locked(sell_ucids):
        return 11,{'msg':utils.get_msg('card','locked')}
    #检查武将是否在deck中
    rc,msg = check_card_in_deck(user_card_obj,sell_ucids)
    if rc:
        return rc,{'msg':msg}
    sell_cards = [user_card_obj.cards[ucid] for ucid in sell_ucids]
    return 0,{'cards_info':sell_cards,'cards_ucids':sell_ucids}
#print 'card_stove() ****************************************'
#print card_stove()


def test_stove():
    from apps.logics.mystery_store import stove
    params = {'category':'card', 'sell_ucids': '201412051105110587210'}    
    pprint (stove(rk_user, params))
test_stove()




def get_store_info():
    """
    得到当前玩家的神秘商店信息
    前段点击 和 前段倒计时结束时调用此接口 神秘商店时调用此接口
     此接口会先判断是否要自动刷新商品
    """
    user_property_obj = UserProperty.get_instance(uid) 
    print user_property_obj.get_fight_soul
    user_mystery_store_obj = UserMysteryStore.get_instance(uid)
    #return 0, _pack_store_info(user_mystery_store_obj.auto_refresh_store())
    k =  _pack_store_info(user_mystery_store_obj.auto_refresh_store())
    print 'data=',json.dumps(k,indent=1)

def _pack_store_info(store_info):
    store_info = copy.deepcopy(store_info)
    #for package in store_info["packages"]:
    #    new_goods = []
    #    for goods in package["goods"]:
    #        new_goods.append(_pack_goods(goods))
    #    package["goods"] = new_goods

    #for goods_info in store_info["gold_store"]:
    #    goods_info["goods"] = _pack_goods(goods_info["goods"])
    for goods_info in store_info["coin_store"]:
        goods_info["goods"] = _pack_goods(goods_info["goods"])
    for goods_info in store_info["fight_soul_store"]:
        goods_info["goods"] = _pack_goods(goods_info["goods"])
    return store_info

def _pack_goods(award):
    k = award.keys()[0]
    out_key = ""
    if k in ['gold','gacha_pt','coin','stone', 'super_soul','fight_soul']:
        return award
    elif 'card' in k:
        if isinstance(award[k], dict):
            out_key = 'card'
        # 区别是武将还是将魂， 如果是将魂 {'160_card':num}
        elif isinstance(award[k], int):
            out_key = 'normal_soul'
    elif 'equip' in k:
        out_key = 'equip'
    elif 'item' in k:
        out_key = 'item'
    elif 'mat' in k:
        out_key = 'material'
    elif 'soul' in k:
        out_key = 'normal_soul'
        award = {k.replace("soul", "card"): award[k]}
    return {out_key: award}


def refresh_store_by_self():
    """
    玩家主动刷新时  调用此接口
    params  参数需包含 store_type ：  "gold_store"  or  "coin_store"
    """
    game_config.subareas_conf()
    game_config.set_subarea('1') 
    store_type_list = ['coin_store','fight_soul_store']
    needed_cost = game_config.mystery_store["store_refresh_cost"]
    user_property_obj = UserProperty.get_instance(uid)
    # 消耗元宝
    minus_func = getattr(user_property_obj, "minus_coin")

    #根据vip刷新次数
    if not vip.check_limit_recover(user_property_obj,'recover_mystery_store'):
        return 11,{'msg':utils.get_msg('user','max_times')}
    #回复次数+1
    user_property_obj.add_recover_times('recover_mystery_store')
    # 再判断是否 coin or gold  足够
    if not minus_func(needed_cost, 'refresh_mystery_store'):
        return 11,{'msg': utils.get_msg('user', 'not_enough_coin')}
    # 记录 消费元宝log
    #data_log_mod.set_log("ConsumeRecord", rk_user, 
    #                        lv=rk_user.user_property.lv,
    #                        num=needed_cost,
    #                        consume_type='refresh_coin_store',
    #                        before_coin=rk_user.user_property.coin + needed_cost,
    #                        after_coin=rk_user.user_property.coin
    #)

    user_mystery_store_obj = UserMysteryStore.get_instance(uid)
    for store_type  in store_type_list:
        user_mystery_store_obj.refresh_store(store_type)
    #return 0, _pack_store_info(user_mystery_store_obj.store_info())
    k = _pack_store_info(user_mystery_store_obj.store_info())
    print 'data=',json.dumps(k,indent=1)

def buy_store_goods():
    """
    玩家购买指定商品时逻辑
    params  参数需包含 store_type： 可选  "packages"   "gold_store"  or  "coin_store" 
                     goods_index:  int  为所买商品在所属类型的index   
    """
    #store_type = params['store_type']
    store_type = 'fight_coin_store'
    goods_index = 1

    buy_goods_info = {}
    goods_list = []
    user_mystery_store_obj = UserMysteryStore.get_instance(uid)

    buy_goods_info = user_mystery_store_obj.store_info()[store_type][goods_index]
    goods_list.append(buy_goods_info['goods'])
    fight_or_coin = "coin" if buy_goods_info.get("coin", 0) else "fight_soul"
    needed_cost = buy_goods_info.get(fight_or_coin, 0)
   
    user_property = UserProperty.get_instance(uid)
    #  根据store_type  决定是 消耗元宝还是战魂
    minus_func = getattr(user_property, "minus_" + fight_or_coin)

    if not minus_func(needed_cost, 'buy_mystery_store_goods'):
         return 11, {'msg': utils.get_msg('user', 'not_enough_' + fight_or_coin)}

    # 发商品    
    # 前端通过rc 是否等于 0 判断是否购买成功
    if not user_mystery_store_obj.update_goods_info_by_index(store_type, goods_index):
        return 11, {'msg': 'has bought this item'}
    all_get_goods = {}
    award_return = {'stamina':0,'gold':0,'coin':0,'gacha_pt':0,'fight_soul':0,'stone':0,'item':{}, 'super_soul': 0, 'material':{},'card':{},'equip':{}, 'normal_soul': {},}

    for goods in goods_list:
        tmp = user_property.test_give_award(_pack_goods(goods), where=u"buy_from_mystery_store")
        for _k in tmp:
            if _k in ['gold','coin','gacha_pt','stone', 'fight_soul','super_soul','stamina']:
                award_return[_k] = award_return.get(_k,0) + tmp.get(_k,0)
            elif _k in ['item','material', 'normal_soul']:
                for __kk in tmp[_k]:
                    award_return[_k][__kk] = award_return[_k].get(__kk,0) + tmp[_k][__kk]
            elif _k in ['card','equip']:
                award_return[_k].update(tmp[_k])
    all_get_goods = {i: award_return[i] for i in award_return if award_return[i]}


    return 0, {'get_info': all_get_goods}

#print buy_store_goods()
