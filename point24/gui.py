# enconding:utf-8

import tkinter as tk
import random
from point24 import *

class Window:
    def __init__(self, title='24点', width=650, height=400):
        B_WIDTH = 6
        B_HEIGHT = 5
        TEN_OR_K = 10
        self.w = width
        self.h = height
        self.tkwindow = tk.Tk(className=title)
        self.label_ans = tk.Label(text="answer", fg="black", bg="white")
        self.label_ans.pack()
        self.opdict = {'+': add, '-': minus, '*': multiply, '/': divide}
        
        self.num1 = random.randint(1, TEN_OR_K)
        self.num2 = random.randint(1, TEN_OR_K)
        self.num3 = random.randint(1, TEN_OR_K)
        self.num4 = random.randint(1, TEN_OR_K)
        
        self.op_pressed = False
        self.op_now = ''
        self.opnum = 0
        self.num_temp = 0
        self.num_count = 0
        self.op_can_use = False
        self.btn_num_temp_used = False
        
        # 数字按钮
        self.btn_num1 = tk.Button(self.tkwindow, text=self.num1, command=self.command_num1,
                                  width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_num1.pack(side='left')
        
        self.btn_num2 = tk.Button(self.tkwindow, text=self.num2, command=self.command_num2,
                                  width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_num2.pack(side='left')
        
        self.btn_num3 = tk.Button(self.tkwindow, text=self.num3, command=self.command_num3,
                                  width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_num3.pack(side='left')
        
        self.btn_num4 = tk.Button(self.tkwindow, text=self.num4, command=self.command_num4,
                                  width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_num4.pack(side='left')

        self.btn_num_temp = tk.Button(self.tkwindow, text=self.num_temp, command=self.command_num_temp,
                                  width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_num_temp.pack(side='bottom')  

        # 操作符按钮
        self.btn_add = tk.Button(self.tkwindow, text='+', command=self.command_add,
                                 width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_add.pack(padx=1, side='left')
        
        self.btn_minus = tk.Button(self.tkwindow, text='-', command=self.command_minus,
                                   width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_minus.pack(padx=1, side='left')
        
        self.btn_multiply = tk.Button(self.tkwindow, text='*', command=self.command_multipy,
                                      width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_multiply.pack(padx=1, side='left')
        
        self.btn_divide = tk.Button(self.tkwindow, text='/', command=self.command_divide,
                                    width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_divide.pack(padx=1, side='left')

        # 功能按钮
        self.btn_change = tk.Button(self.tkwindow, text='换一组', command=self.command_change,
                                    width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_change.pack(padx=1, side='right')

        self.btn_answer = tk.Button(self.tkwindow, text='显示答案', command=self.command_answer,
                                 width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_answer.pack(padx=1, side='right')
        
        self.btn_answer = tk.Button(self.tkwindow, text='清除', command=self.command_clear,
                                 width=B_WIDTH, height=B_HEIGHT,relief='groove')
        self.btn_answer.pack(padx=1, side='right')

    # 一个数字只能按一次，按错了用clear重来
    def command_clear(self):
        self.btn_num1['state'] = 'active'
        self.btn_num2['state'] = 'active'
        self.btn_num3['state'] = 'active'
        self.btn_num4['state'] = 'active'
        self.btn_num_temp['state'] = 'active'
        self.btn_num_temp['text'] = '0'
        self.label_ans['text'] = 'answer'
        self.num_temp = 0
        self.op_pressed = False
        self.op_now = ''
        self.opnum = 0
        self.num_temp = 0
        self.btn_num_temp_used = False
        self.num_count = 0       

    def command_answer(self):
        ans = cal_24point(self.num1, self.num2, self.num3, self.num4)
        self.label_ans['text'] = str(ans)

    def command_change(self):

        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.num3 = random.randint(1, 10)
        self.num4 = random.randint(1, 10)
        self.btn_num1['text'] = self.num1
        self.btn_num2['text'] = self.num2
        self.btn_num3['text'] = self.num3
        self.btn_num4['text'] = self.num4
        self.command_clear()

    def command_add(self):
        if self.op_can_use:
            self.op_now = '+'
            self.op_pressed = True

    def command_minus(self):
        if self.op_can_use:
            self.op_now = '-'
            self.op_pressed = True

    def command_multipy(self):
        if self.op_can_use:
            self.op_now = '*'
            self.op_pressed = True

    def command_divide(self):
        if self.op_can_use:
            self.op_now = '/'
            self.op_pressed = True

    def command_num_temp(self):
        if self.op_pressed:
            self.opnum = self.opdict[self.op_now](self.opnum, self.num_temp)[0]
            self.btn_num_temp['text'] = self.opnum
            self.num_temp = self.opnum
        else:
            self.opnum = self.num_temp
        print(self.opnum)
        self.op_pressed = False
        self.btn_num_temp['state'] = 'disabled'

        if self.opnum == 24:
            self.label_ans['text'] = 'right'

    def command_num1(self):
        if self.op_pressed:
            self.opnum = self.opdict[self.op_now](self.opnum, self.num1)[0]
            if not self.btn_num_temp_used:
                self.btn_num_temp['text'] = self.opnum
                self.num_temp = self.opnum
                self.btn_num_temp_used = True
        else:
            self.opnum = self.num1
        print(self.opnum)
        self.op_pressed = False
        self.btn_num1['state'] = 'disabled'
        self.op_can_use = True
        self.num_count += 1
        if self.opnum == 24 and self.num_count ==4:
            self.label_ans['text'] = 'right'

    def command_num2(self):
        if self.op_pressed:
            self.opnum = self.opdict[self.op_now](self.opnum, self.num2)[0]
            if not self.btn_num_temp_used:
                self.btn_num_temp['text'] = self.opnum
                self.num_temp = self.opnum
                self.btn_num_temp_used = True
        else:
            self.opnum = self.num2
        print(self.opnum)
        self.op_pressed = False
        self.btn_num2['state'] = 'disabled'
        self.op_can_use = True
        self.num_count += 1
        if self.opnum == 24 and self.num_count ==4:
            self.label_ans['text'] = 'right'

    def command_num3(self):
        if self.op_pressed:
            self.opnum = self.opdict[self.op_now](self.opnum, self.num3)[0]
            if not self.btn_num_temp_used:
                self.btn_num_temp['text'] = self.opnum
                self.num_temp = self.opnum
                self.btn_num_temp_used = True
        else:
            self.opnum = self.num3
        print(self.opnum)
        self.op_pressed = False
        self.btn_num3['state'] = 'disabled'
        self.op_can_use = True
        self.num_count += 1
        if self.opnum == 24 and self.num_count ==4:
            self.label_ans['text'] = 'right'

    def command_num4(self):
        if self.op_pressed:
            self.opnum = self.opdict[self.op_now](self.opnum, self.num4)[0]
            if not self.btn_num_temp_used:
                self.btn_num_temp['text'] = self.opnum
                self.num_temp = self.opnum
                self.btn_num_temp_used = True
        else:
            self.opnum = self.num4
        print(self.opnum)
        self.op_pressed = False
        self.btn_num4['state'] = 'disabled'
        self.op_can_use = True
        self.num_count += 1
        if self.opnum == 24 and self.num_count ==4:
            self.label_ans['text'] = 'right'

    def center(self):
        ws = self.tkwindow.winfo_screenwidth()
        hs = self.tkwindow.winfo_screenheight()
        x = int( (ws/2) - (self.w/2) )
        y = int( (hs/2) - (self.h/2) )
        self.tkwindow.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def loop(self):
        self.tkwindow.resizable(False, False)
        self.center()
        self.tkwindow.mainloop()

# ##############################run#########################################
w = Window()
w.loop()
