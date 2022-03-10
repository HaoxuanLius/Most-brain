import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem


class DoubancrawerSpider(scrapy.Spider):
    name = 'doubancrawer'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['https://www.xiachufang.com/explore/']

    


    def parse(self, response):
        b=BeautifulSoup(response.text,'html.parser')
        e=b.find_all('div',class_='info pure-u')
        for i in e:
            url='http://www.xiachufang.com'+i.find('a')['href']
            yield scrapy.Request(url,callback=self.parse_da)

    def parse_da(self,response):
        items=DoubanItem()
        b=BeautifulSoup(response.text,'html.parser')
        e=b.find_all('td',class_='name')
        f=b.find_all('td',class_='unit')
        g=e=b.find_all('li',class_='container')
        items['daoy']=' '.join([g.text.strip()+': '+h.text.strip() for g,h in zip(e,f)])
        items['name']=b.find('h1',class_='page-title').text.strip()
        items['time']='\n'.join([str(b)+a.text.strip() for a,b in zip(g,range(1,len(g)))])
        yield items



