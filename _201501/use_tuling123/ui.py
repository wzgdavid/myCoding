# encoding: utf-8
 
import Tkinter as tk
import random
import utils
import datetime
from chat import TulingChat
import time
import tkFont


class Window:
    def __init__(self, title='机器人吉米', width=650, height=600):
 
        self.w = width
        self.h = height
        self.tkwindow = tk.Tk(className=title)
        self.init_status()
        self.add_compnent()
 
    def init_status(self):
        pass

 
    def add_compnent(self):
        B_WIDTH = 6
        B_HEIGHT = 5
 
        self.label_ans = tk.Label(text="answer", fg="black", bg="white")
        self.label_ans.pack()
 
        # 发送按钮
        self.btn_send = tk.Button(self.tkwindow, text='发送',
                                command=self.command_send_message,
                                width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_send.pack(side='right')
 
 
        # 功能按钮
        #self.btn_change = tk.Button(self.tkwindow, text='换一组',
        #                            command=self.command_num1,
        #                            width=B_WIDTH, height=B_HEIGHT,relief='groove')
        #self.btn_change.pack(padx=1, side='right')
 
        # 显示框
        myFont = tkFont.Font(size=15)
        self.show_text = tk.Text(self.tkwindow, height=20, font=myFont)
        self.show_text.insert(tk.INSERT, "Hello.....")
        self.show_text.insert(tk.END, "Bye Bye.....\n")
        self.show_text.insert(tk.END, "hei hei.....")

        self.show_text.tag_add("here", tk.INSERT, tk.END)
        #self.show_text.tag_add("start", "1.8", "1.13")
        self.show_text.tag_config("here", background="green", foreground="black")
        #self.show_text.tag_config("start", background="black", foreground="green")
 
        self.show_text.pack(side='top')


        # 输入框
        self.input_text = tk.Text(self.tkwindow, height=5,  font=myFont)
        self.input_text.pack(side='top')

    def command_num1(self):
        print 'command done'

    def command_send_message(self):
        #print tk.END, type(tk.END)
        msg = self.input_text.get('1.0', tk.END)[:-1].encode('utf-8')
        #print 'type(msg)', type(msg), msg, len(msg)
        if not msg:
            #print 'invalid msg'
            return
        self.input_text.delete('1.0', tk.END)
        now_time = utils.datetime_toString(datetime.datetime.now()).split(' ')[1]

        self.show_text.insert(tk.END, now_time + '\n' + msg + "\n\n")
        chat = TulingChat()

        rtn_msg = chat.send_message(msg)
        self.show_text.insert(tk.END, now_time + '\n' + rtn_msg + "\n\n")

 
    def center(self):
        ws = self.tkwindow.winfo_screenwidth()
        hs = self.tkwindow.winfo_screenheight()
        x = int((ws/2)-(self.w/2))
        y = int((hs/2)-(self.h/2))
        self.tkwindow.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))
 
    def loop(self):
        self.tkwindow.resizable(True, True)
        self.center()
        self.tkwindow.mainloop()
 
if __name__ == "__main__":
    w = Window()
    w.loop()
