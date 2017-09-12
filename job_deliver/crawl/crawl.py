# encoding:utf-8 
import sys
sys.path.append('e:/workspace/job_deliver')
import requests
import pymongo
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
#from bs4 import BeautifulSoup
from lxml import etree
from db.mysql.models import session, Applied_job
from db.mysql.conf import engine
from sqlalchemy.exc import IntegrityError, InvalidRequestError
#import pymysql.err.IntegrityError
#login_page = 'https://login.51job.com/login.php'
#r = requests.get(login_page)
#r.encoding = r.apparent_encoding

class Crawl_51(object):
    login_url = 'https://login.51job.com/login.php'
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.all_apply = []
    def login(self):
        
        self.driver.get(self.login_url)
        loginname = self.driver.find_element_by_id('loginname')
        loginname.clear()
        loginname.send_keys("wzgdavid")
        password = self.driver.find_element_by_id('password')
        password.clear()
        password.send_keys("741852tgb")
        
        login_btn = self.driver.find_element_by_id('login_btn')
        login_btn.click()

        time.sleep(1)
        current_window = self.driver.current_window_handle # 转到当前页面
        #print self.driver.current_url
        #link = self.driver.find_element_by_xpath('//a[@href="http://i.51job.com/userset/my_apply.php?lang=c"]')
        self.driver.get("http://i.51job.com/userset/my_apply.php?lang=c")# 
        current_window = self.driver.current_window_handle
        #print dir(self.driver) # ['CONTEXT_CHROME', 'CONTEXT_CONTENT', 'NATIVE_EVENTS_ALLOWED', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_file_detector', '_is_remote', '_mobile', '_switch_to', '_unwrap_value', '_web_element_cls', '_wrap_value', 'add_cookie', 'application_cache', 'back', 'binary', 'capabilities', 'close', 'command_executor', 'context', 'create_web_element', 'current_url', 'current_window_handle', 'delete_all_cookies', 'delete_cookie', 'desired_capabilities', 'error_handler', 'execute', 'execute_async_script', 'execute_script', 'file_detector', 'file_detector_context', 'find_element', 'find_element_by_class_name', 'find_element_by_css_selector', 'find_element_by_id', 'find_element_by_link_text', 'find_element_by_name', 'find_element_by_partial_link_text', 'find_element_by_tag_name', 'find_element_by_xpath', 'find_elements', 'find_elements_by_class_name', 'find_elements_by_css_selector', 'find_elements_by_id', 'find_elements_by_link_text', 'find_elements_by_name', 'find_elements_by_partial_link_text', 'find_elements_by_tag_name', 'find_elements_by_xpath', 'firefox_profile', 'forward', 'get', 'get_cookie', 'get_cookies', 'get_log', 'get_screenshot_as_base64', 'get_screenshot_as_file', 'get_screenshot_as_png', 'get_window_position', 'get_window_rect', 'get_window_size', 'implicitly_wait', 'log_types', 'maximize_window', 'mobile', 'name', 'orientation', 'page_source', 'profile', 'quit', 'refresh', 'save_screenshot', 'service', 'session_id', 'set_context', 'set_page_load_timeout', 'set_script_timeout', 'set_window_position', 'set_window_rect', 'set_window_size', 'start_client', 'start_session', 'stop_client', 'switch_to', 'switch_to_active_element', 'switch_to_alert', 'switch_to_default_content', 'switch_to_frame', 'switch_to_window', 'title', 'w3c', 'window_handles']
        thepage = self.driver.page_source
        time.sleep(1)
        #print thepage.decode('utf-8') # 可以打印出当前页面

    def jump_to_page(self, page_num):
        jump_page = self.driver.find_element_by_id('jump_page')
        jump_page.clear()
        jump_page.send_keys(str(page_num))
        confirm = self.driver.find_element_by_xpath('//div[@class="p_in"]/span[3]') # 确定
        confirm.click()
        self.driver.current_window_handle
        time.sleep(1)
        #return self.driver.page_source.decode('utf-8')
    
    def can_jumpto_next_page(self):
        selector = etree.HTML(self.driver.page_source)
        a = selector.xpath('//div[@class="dw_page"]/div/div/div/ul/li[last()]/a')
        #没有下一页时，下一页的li里没有a，有a就有下一页
        if len(a) != 0:
            return True
        return False

    def get_data_from_page(self):
        #soup = BeautifulSoup(self.driver.page_source, 'lxml')
        #alla = soup.find_all('a')
        #print alla
        #                            职位名  公司名  工作地点 薪资      申请日期     申请的简历      近两周申请      进度
        #one_apply = dict.fromkeys(['job','company', 'place', 'salary', 'apply_date', 'resume_name', 'recent_apply', 'rate'])
        onepage_apply = []
        selector = etree.HTML(self.driver.page_source)
        jobs = selector.xpath('//div[@class="rli"]/ul/li[1]/a/text()') # 要strip
        companies = selector.xpath('//div[@class="rli"]/ul/li[2]/a/text()') # 要strip
        places = selector.xpath('//div[@class="rli"]/ul/li[3]/text()')
        salaries = selector.xpath('//div[@class="rli"]/ul/li[4]/text()')
        apply_dates = selector.xpath('//div[@class="rli"]/ul/li[5]/text()')
        resume_names = selector.xpath('//div[@class="rsp"]/ul/li[1]/span/text()')
        recent_applies = selector.xpath('//div[@class="rsp"]/ul/li[2]/span/text()')
        job_urls =  selector.xpath('//div[@class="rli"]/ul/li[1]/a/@href')
        #rates = selector.xpath('//div[@class="rate"]/div/em/text()')
        #print job_urls
        for i in range(len(jobs)):
            try:
                one_apply = dict.fromkeys(['job','company', 'place', 'salary', 'apply_date', 'resume_name', 'recent_apply', 'rate'])
                one_apply['job'] = jobs[i].strip()
                one_apply['company'] = companies[i].strip()
                one_apply['place'] = places[i]
                one_apply['salary'] = salaries[i]
                one_apply['apply_date'] = apply_dates[i]
                one_apply['resume_name'] = resume_names[i]
                one_apply['recent_apply'] = int(recent_applies[i])
                one_apply['rate'] = None
                one_apply['job_url'] = job_urls[i]
            except IndexError, e:
                #self.driver.close()
                pass

            #one_apply['rate'] =
            #print one_apply
            onepage_apply.append(one_apply)
        return onepage_apply
        
    def save_to_mongodb(self):
        client = MongoClient('localhost', 27017)
        db = client['test']
        collection = db['test']
        for n in self.all_apply:
            try:
                collection.insert(n)
            except pymongo.errors.DuplicateKeyError:
                #self.driver.close()
                print 'E11000 duplicate key'
                #break
        self.driver.close()

    def save_to_mysql(self, onepage_apply):
        #ajs = []
        #for n in self.all_apply:
        #    ajs.append(Applied_job(**n))
        #session.add_all(ajs)
        #try:
        #    session.commit()
        #except IntegrityError, e:
        #    pass
        #session.close()
        
        for n in onepage_apply:
            
            try:
                #session.add(Applied_job(**n))
                #session.commit()
                Applied_job(**n).save()
            except (IntegrityError, InvalidRequestError): # 已经save过的数据，停止操作
                #raise IntegrityError
                session.rollback()
                print '已经save过的数据'
                raise Exception
                break
                
        

    def _generate_one_apply(self):
        #                            职位名  公司名  工作地点 薪资      申请日期     申请的简历      近两周申请      进度
        one_apply = dict.fromkeys(['job','company', 'place', 'salary', 'apply_date', 'resume_name', 'recent_apply', 'rate'])
        print one_apply

    def run(self):
        self.get_data_from_page()
        for n in range(1, 9999):
            if self.can_jumpto_next_page():
                self.jump_to_page(n)
                onepage_apply = self.get_data_from_page()
                #self.save_to_mysql(onepage_apply)
                try:
                    self.save_to_mysql(onepage_apply)
                except Exception, e:
                    break
                
            else:
                break 
        #session.close()  
        self.driver.close()


def test_crawl():
    c = Crawl_51()
    c.login()
    c.run()
    c.save_to_mongodb()    

def refresh_applied_jobs():
    '''把最新的申请加入mysql'''
    c = Crawl_51()
    c.login()
    c.run()

if __name__ == '__main__':
    refresh_applied_jobs()

    pass
    

   
