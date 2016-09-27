import requests
from bs4 import BeautifulSoup


#browser = webdriver.Firefox()
#browser.get('https://www.baidu.com/')

#import random
#def sequence(length=99):

def foo(runto, step=1):
    '''
    runto   times of atr,a float,
    step    jia cang dian wei ji ge atr
    '''
    total = 0
    jc = int(runto // step) # jia cang ci shu
    for n in range(1, jc+1):
        print n
    

if __name__ == '__main__':
    foo(12.1, step=3)