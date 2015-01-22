# encoding: utf-8
#from __future__ import print_function, unicode_literals, absolute_import

# 问题是 怎么清除输入框， 输入框字超出框框时不会自动滚动

import datetime
import toga
import utils
from chat import TulingChat

def build(app):
    container = toga.Container()

    #show_msg = toga.TextInput(readonly=True)
    show_msg = toga.TextInput()
    input_msg = toga.TextInput()

    def send_msg(widget):
        msg = input_msg.value  # type unicode
        if len(msg) == 0: return
        #print(type(msg), '----'*10)
        now_time = utils.datetime_toString(datetime.datetime.now()).split(' ')[1]
        show_msg.value += now_time + '\n' + msg + '\n\n'

        chat = TulingChat()
        rtn_msg = chat.send_message(msg.encode('utf-8').strip())
        show_msg.value += now_time + '\n' + rtn_msg + '\n\n'

        #print dir(container)
        #print input_msg.value, 'input_msg.value'

    button = toga.Button(u'发送', on_press=send_msg)
    container.add(input_msg)
    container.add(show_msg)
    container.add(button)

    container.constrain(show_msg.HEIGHT == 500)
    container.constrain(show_msg.TOP == container.TOP + 20)
    container.constrain(show_msg.LEFT == container.LEFT + 20)
    container.constrain(show_msg.RIGHT == container.RIGHT - 20)

    container.constrain(input_msg.HEIGHT == 100)
    container.constrain(input_msg.WIDTH == show_msg.WIDTH)
    container.constrain(input_msg.TOP == show_msg.BOTTOM + 20)
    container.constrain(input_msg.LEADING == show_msg.LEADING)

    container.constrain(button.TOP == input_msg.BOTTOM + 20)
    container.constrain(button.LEADING == input_msg.LEADING)
    container.constrain(button.BOTTOM + 20 == container.BOTTOM)

    return container


if __name__ == '__main__':
    app = toga.App(u'机器人吉米', 'personel.wzg', startup=build)
    app.main_loop()
