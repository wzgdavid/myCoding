#encoding: utf-8
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import pprint as pp
import urllib 
import MySQLdb

_HOUSING_IMG_PATH = '/home/david/crawlhousing/images/housing/'

conn = MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='1',
        db ='mysite',
    )

def get_soup(url):
    r = requests.get(url)
    soup = None
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
    return soup
     
def get_data(soup):
    data = {}
    if not soup:
        print 'can not find the html'
        return None

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
        item_name = li.string.strip().lower().replace(' ', '-')
        if li.attrs['class'][0].strip() == 'black':
            data[item_name] = 1
        else:
            data[item_name] = 0

    imgs = soup.find_all('img', class_='lightboxable')
    for n in imgs:
        url = n.attrs['src']
        filename = _HOUSING_IMG_PATH + url.split('/')[-1]
        #print filename
        urllib.urlretrieve(url, filename)

    pp.pprint(data)
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
  `floor` VARCHAR(3) NULL,
  `furnished` VARCHAR(45) NULL,
  `internet` VARCHAR(45) NULL,
  `metro` VARCHAR(200) NULL,
  `housingcol` VARCHAR(45) NULL,
  `rooms` VARCHAR(200) NULL,
  `size` VARCHAR(45) NULL,
  `air-filter` TINYINT NULL DEFAULT 0,
  `balcony` TINYINT NULL DEFAULT 0,
  `central-aircon` TINYINT NULL DEFAULT 0,
  `dryer` TINYINT NULL DEFAULT 0,
  `dvd-player` TINYINT NULL DEFAULT 0,
  `elevator` TINYINT NULL DEFAULT 0,
  `health-club` TINYINT NULL DEFAULT 0,
  `outdoor-space` TINYINT NULL DEFAULT 0,
  `oven` TINYINT NULL DEFAULT 0,
  `parking` TINYINT NULL DEFAULT 0,
  `playground` TINYINT NULL DEFAULT 0,
  `pool` TINYINT NULL DEFAULT 0,
  `security` TINYINT NULL DEFAULT 0,
  `tv` TINYINT NULL DEFAULT 0,
  `washing-machine` TINYINT NULL DEFAULT 0,
  `water-filter` TINYINT NULL,
  PRIMARY KEY (`id`));
'''
def save_to_db(data):
    pass


if __name__ == '__main__':
    soup = get_soup('http://www.smartshanghai.com/housing/service-apartments/692114')
    data = get_data(soup)

    #print(soup.prettify())
    #print soup.title.string
    #title = soup.find('div', class_='mingzi')
    #print rmeta.attrs['content']
    #print soup.find('div', class_='mingzi').string
    #link = soup.find('div', class_='link')
    #print soup.find('div', class_='link').find_all('div')[1].text.strip()
    #fn = soup.find('div', class_='fast-navigation').find_all('li')
    
    #for n in fn:
    #    print n.attrs['class'][0]
    #    print n.string.strip().lower()