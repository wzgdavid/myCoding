# encoding: utf-8
import scrapy


'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
'''

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.autohome.com.cn/a/4_29-1.1_1.6-0-0-1-0-1-1-0-0/',
    ]

    def parse(self, response):
        
        '''yield {
                'car_urls': response.xpath('//div[@class="rank-list"]/dl/dd/ul/li/h4/a/@href').extract(),
                
        }'''

        car_pages = response.xpath('//dd/ul/li/h4/a[1]/@href').extract()
        #print '*********************-----********************'

        if len(car_pages) > 0:
            for page in car_pages:
                #print page
                yield scrapy.Request(response.urljoin(page),
                                 callback=self.parse_car_page)

    def parse_car_page(self, response):
        '''
        爬取汽车页面 
        like
        http://www.autohome.com.cn/554/#levelsource=000101104_29&pvareaid=101594
        '''

        
        # 口碑
        koubei_page = response.xpath('//div[@id="navTop"]/ul/li[5]/a/@href').extract_first()
        #print '---------------', koubei_page
        if koubei_page is not None:
            koubei_page = response.urljoin(koubei_page)
            yield scrapy.Request(koubei_page, callback=self.parse_koubei)

        # 参数
        canshu_page = response.xpath('//div[@id="navTop"]/ul/li[2]/a/@href').extract_first()
        if canshu_page is not None:
            canshu_page = response.urljoin(canshu_page)
            yield scrapy.Request(canshu_page, callback=self.parse_canshu)



    def parse_koubei(self, response):
        '''
        爬取口碑页面 like
        http://k.autohome.com.cn/554/
        '''
        #print '-------------parse_koubei '
        score = response.xpath('//div[@id="0"]/dl/dd/ul/li[2]/span[1]/span[2]/text()').extract_first()
        if score is not None:
            score = float(score)
        data ={
            'car_name': response.xpath('//div[@class="subnav-title"]/div/a/text()').extract_first(), 
            'score':  score # 用户口碑评分
        }


        yield data

    def parse_canshu(self, response):
        '''
        爬取参数页面 like
        http://car.autohome.com.cn/config/series/2429.html
        ''' 
        Nm = 1