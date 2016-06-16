#encoding: utf-8
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import pprint as pp


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

    data['title'] = soup.find('div', attrs={'class': 'mingzi'}).text.strip()

    xinxi = soup.find('div', attrs={'class': 'xinxi'}).find_all('li')
    for n in xinxi:
        item_name = n.find('div', attrs={'class': 'shuxin'}).text.strip().strip(':').lower()
        #print item_name
        value = n.find('div', attrs={'class': 'wenzi'}).text.strip()
        #print value
        data[item_name] = value

    data['description'] = soup.find('div', attrs={'class': 'link'}).find_all('div')[1].text.strip()
    
    fn_lists = soup.find('div', attrs={'class': 'fast-navigation'}).find_all('li')
    for li in fn_lists:
        item_name = li.string.strip().lower().replace(' ', '-')
        if li.attrs['class'][0].strip() == 'black':
            data[item_name] = 1
        else:
            data[item_name] = 0
    pp.pprint(data)
    return data

if __name__ == '__main__':
    soup = get_soup('http://www.smartshanghai.com/housing/service-apartments/692295')
    get_data(soup)

    #print(soup.prettify())
    #print soup.title.string
    #title = soup.find('div', attrs={'class': 'mingzi'})
    #print rmeta.attrs['content']
    #print soup.find('div', attrs={'class': 'mingzi'}).string
    #link = soup.find('div', attrs={'class': 'link'})
    #print soup.find('div', attrs={'class': 'link'}).find_all('div')[1].text.strip()
    #fn = soup.find('div', attrs={'class': 'fast-navigation'}).find_all('li')
    
    #for n in fn:
    #    print n.attrs['class'][0]
    #    print n.string.strip().lower()