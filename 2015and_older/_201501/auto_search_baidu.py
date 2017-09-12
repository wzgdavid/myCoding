#!/usr/bin/env python
#-*-coding:utf-8-*-

import pyautogui as pag
import webbrowser
import time

def search_from_baidu(keyword):
    __open_browser('http://www.baidu.com/')
    __click(583, 381)
    pag.typewrite(keyword, interval=0.2)
    time.sleep(0.5)
    pag.press('enter')

def __click(x, y):
    pag.moveTo(x, y)
    pag.click()

def __open_browser(url):
    webbrowser.open(url)
    time.sleep(1) 

search_from_baidu('python')