#codin: utf-8
from utils import selectDB
"""
    LOG_TABLES

buildupdate
cardconsume
carddeck
cardproduct
cardupdate
cardupgrade
chargerecord
chargeresultlog
coinconsume
coinproduct
consumerecord
dungeonrecord
equconsume
equproduct
feed
goldconsume
goldproduct
invite
itemconsume
itemproduct
loginrecord
matconsume
matproduct
newguide
pvprecord
stoneconsume
stoneproduct
system.indexes
system.users
userlevelhistory
"""

import pdb; pdb.set_trace()
table = selectDB.db('cn', 'log').cardupgrade

print table.count()
