# encoding: utf-8
#from __future__ import print_function, unicode_literals, absolute_import

# 问题是 怎么清除输入框， 输入框字超出框框时不会自动滚动


import toga
from math import ceil
from TexasHold_em import TexasHold_em


def build(app):
    container = toga.Container()

    #show_msg = toga.TextInput(readonly=True)
    show_msg = toga.TextInput()
    public_cards = []
    my_pocket_cards = []

    def send_msg(widget):
        print 'button dir', dir(widget)
        print widget.label
        pass

    def select_card(widget):
        print widget.label
        
        pass


        #print dir(container)
        #print input_msg.value, 'input_msg.value'
    c_label = toga.Label(u'花色(s-spades黑桃 h-hearts红桃 d-diamonds方块 c-clubs梅花)', alignment=toga.LEFT_ALIGNED)
    container.add(c_label)
    people_num_label = toga.Label(u'输入人数', alignment=toga.LEFT_ALIGNED)
    container.add(people_num_label)

    button = toga.Button(u'计算', on_press=send_msg)
    
    container.add(show_msg)
    container.add(button)

    container.constrain(show_msg.HEIGHT == 20)
    container.constrain(show_msg.TOP == container.TOP + 20)
    container.constrain(show_msg.LEFT == container.LEFT + 20)
    container.constrain(show_msg.RIGHT == container.RIGHT - 20)


    container.constrain(button.TOP == show_msg.BOTTOM)
    #container.constrain(button.LEADING == show_msg.LEADING)
    container.constrain(button.BOTTOM + 500 == container.BOTTOM)
    # suit: 花色(s-spades黑桃 h-hearts红桃 d-diamonds方块 c-clubs梅花)

    #card_s2 = toga.Button('s_2', on_press=select_card); container.add(card_s2)
    #container.constrain(card_s2.TOP == show_msg.BOTTOM + 20)
#
    #card_s3 = toga.Button('s_3', on_press=select_card); container.add(card_s3)
    #container.constrain(card_s3.TOP == card_s2.BOTTOM + 10)
    #card_s4 = toga.Button('s_4', on_press=select_card); container.add(card_s4)
    #container.constrain(card_s4.TOP == card_s3.BOTTOM + 10)

    suits = ['s', 'h', 'd', 'c']
    num = [str(n) for n in range(2, 11)]
    num.extend(['J', 'Q', 'K', 'A'])
    cards_lst = []
    for s in suits:
        for n in num:
            cards_lst.append(toga.Button(s+'_'+n, on_press=select_card))
    for n, card in enumerate(cards_lst):
        container.add(card)
        container.constrain(card.TOP == show_msg.BOTTOM + 30*((n+1)%13))
        container.constrain(card.LEFT == container.LEFT + 60*( ceil((n+1)/13.0) ) )

    return container


if __name__ == '__main__':
    app = toga.App(u'德州', 'personel.wzg', startup=build)
    app.main_loop()
