#encoding: utf-8
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import pprint as pp
import urllib 
import MySQLdb
import json
import gevent
from gevent import monkey; monkey.patch_all()



_HOUSING_IMG_PATH = '/home/david/crawlhousing/images/housing/'

conn = MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='1',
        db ='mysite',
    )


def get_item_urls(page_url, start=1, end=1):
    '''
    page_url    like http://www.smartshanghai.com/housing/shared-apartments/
    current_url like http://www.smartshanghai.com/housing/shared-apartments/?page=2
    item_url    like http://www.smartshanghai.com/housing/shared-apartments/691102
    '''
    pages = range(start, end+1)
    current_urls = []
    item_urls = set()
    for n in pages:
         current_urls.append(page_url+'?page='+str(n))
    #print current_urls
    for current_url in current_urls:
        
        soup = get_soup(current_url)
        #print soup
        if not soup:
            break
        print current_url+'-----------'
        biaotis = soup.find('div', class_='content-inside').find_all('div', class_='biaoti')
        for biaoti in biaotis:
            item_urls.add(biaoti.a.attrs['href'])
    #print item_urls
    return item_urls

def get_soup(url):
    r = requests.get(url)
    soup = None
    #print r.status_code
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
    return soup
     
def get_data(url):
    soup = get_soup(url)
    if not soup:
        print 'can not find the html'
        return None

    data = {}
    data['id'] = int(url.split('/')[-1])
    data['title'] = soup.find('div', class_='mingzi').text.strip()

    xinxi = soup.find('div', class_='xinxi').find_all('li')
    for n in xinxi:
        item_name = n.find('div', class_='shuxin').text.strip().strip(':').lower()
        #print item_name
        #value = n.find('div', attrs={'class': 'wenzi'}).text.strip()
        # same but this is simple than upper one
        value = n.find('div', class_='wenzi').text.strip() 

        #print value
        data[item_name] = value

    data['description'] = soup.find('div', class_='link').find_all('div')[1].text.strip()
    
    fn_lists = soup.find('div', class_='fast-navigation').find_all('li')
    for li in fn_lists:
        item_name = li.string.strip().lower().replace(' ', '_')
        if li.attrs['class'][0].strip() == 'black':
            data[item_name] = 1
        else:
            data[item_name] = 0

    imgs = soup.find_all('img', class_='lightboxable')
    filenames = []
    for n in imgs:
        src = n.attrs['src']
        filename = _HOUSING_IMG_PATH + src.split('/')[-1]
        #print filename
        urllib.urlretrieve(src, filename)
        filenames.append(filename)
    
    data['img_src'] = '_'.join(filenames)
    #pp.pprint(data)
    return data


'''
CREATE TABLE `mysite`.`housing` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(150) NOT NULL,
  `description` TEXT NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `area` VARCHAR(45) NULL,
  `commission` VARCHAR(150) NULL,
  `compound` VARCHAR(45) NULL,
  `floor` VARCHAR(10) NULL,
  `furnished` VARCHAR(45) NULL,
  `internet` VARCHAR(90) NULL,
  `metro` VARCHAR(200) NULL,
  `rooms` VARCHAR(200) NULL,
  `size` VARCHAR(45) NULL,
  `price` VARCHAR(200) NULL,
  `pets` VARCHAR(45) NULL,
  `air_filter` TINYINT NULL DEFAULT 0,
  `balcony` TINYINT NULL DEFAULT 0,
  `central_aircon` TINYINT NULL DEFAULT 0,
  `dryer` TINYINT NULL DEFAULT 0,
  `dvd_player` TINYINT NULL DEFAULT 0,
  `elevator` TINYINT NULL DEFAULT 0,
  `health_club` TINYINT NULL DEFAULT 0,
  `outdoor_space` TINYINT NULL DEFAULT 0,
  `oven` TINYINT NULL DEFAULT 0,
  `parking` TINYINT NULL DEFAULT 0,
  `playground` TINYINT NULL DEFAULT 0,
  `pool` TINYINT NULL DEFAULT 0,
  `security` TINYINT NULL DEFAULT 0,
  `tv` TINYINT NULL DEFAULT 0,
  `washing_machine` TINYINT NULL DEFAULT 0,
  `water_filter` TINYINT NULL DEFAULT 0,
  `img_src` VARCHAR(2000) NULL,
  PRIMARY KEY (`id`));
'''

def save_to_db(data):
    cur = conn.cursor()
    

    try:
        data['commission']
    except KeyError, e:
        data['commission'] = ''

    sql = '''
        insert into housing values({id}, "{title}", "{description}", "{type}", "{area}",
        "{commission}", "{compound}", "{floor}", "{furnished}", "{internet}",  
        "{price}", "{metro}", "{rooms}", "{size}", "{pets}", {air_filter}, 
        {balcony}, {central_aircon}, {dryer}, {dvd_player}, {elevator}, 
        {health_club}, {outdoor_space}, {oven}, {parking}, {playground}, 
        {pool}, {security}, {tv}, {washing_machine}, {water_filter}, 
        "{img_src}")
        '''.format(id=data['id'], title=data['title'],
            description=data['description'],
            type=data['type'],
            area=data['area'],
            commission=data['commission'],
            compound=data['compound'],
            floor=data['floor'],
            furnished=data['furnished'],
            internet=data['internet'],
            price=data['price'],
            metro=data['metro'],
            rooms=data['rooms'],
            size=data['size'],
            pets=data['pets'],
            air_filter=data['air_filter'],
            balcony=data['balcony'],
            central_aircon=data['central_aircon'],
            dryer=data['dryer'],
            dvd_player=data['dvd-player'],
            elevator=data['elevator'],
            health_club=data['health_club'],
            outdoor_space=data['outdoor_space'],
            oven=data['oven'],
            parking=data['parking'],
            playground=data['playground'],
            pool=data['pool'],
            security=data['security'],
            tv=data['tv'],
            washing_machine=data['washing_machine'],
            water_filter=data['water_filter'],
            img_src=data['img_src'],
            )
    #print sql
    cur.execute(sql) 
    cur.close()
    conn.commit()
    #conn.close()



def insert_one_to_db(url):
    data = get_data(url)
    if len(data['title'])> 0:
        save_to_db(data)   

def crawl_page(url, start=1, end=1):
    items = get_item_urls(url, start, end)
    for url in items:
        print url
        try:
          insert_one_to_db(url)
        except Exception, e:
          pass
        
    

if __name__ == '__main__':
    
    #insert_one_to_db('http://www.smartshanghai.com/housing/service-apartments/692117')
    # crawl_page('http://www.smartshanghai.com/housing/commercial-spaces/',end=20)

    # shared-apartments/?page=77
    # apartments-rent/?page=534
    # offices/?page=36

    gevent.joinall([
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/shared-apartments/', end=78),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/apartments-rent/', start=1, end=100),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/apartments-rent/', start=101, end=200),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/apartments-rent/', start=201, end=300),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/apartments-rent/', start=301, end=400),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/apartments-rent/', start=401, end=500),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/service-apartments/', end=6),
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/commercial-spaces/,', end=4),
      
      gevent.spawn(crawl_page, 'http://www.smartshanghai.com/housing/offices/', end=36),
        
    ])


    conn.close()