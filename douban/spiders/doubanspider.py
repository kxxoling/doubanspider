# coding: utf-8
from scrapy.spider import Spider
from lxml import html
from douban.items import DoubanItem


class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/subject/1439831/']
# zxd 'http://movie.douban.com/tag/%E5%8A%A8%E6%BC%AB/',

    def parse(self, response):
        selector = html.fromstring(response.body)

        item = DoubanItem()
        info_div = selector.xpath('//div[@id="info"]')[0]
        info_list = []
        for info_item in info_div.text_content().split('\n'):
            info_list.append(map(lambda x: x.strip()), info_item.split(': '))

        item['name'] = selector.xpath('//span[@property="v:itemreviewed"]/text()')[0]
        item['director'] = [i.text for i in selector.xpath(u'//div[@id="info"]//span[text()="导演"]/following-sibling::a')]
        item['dramatist'] = [i.text for i in selector.xpath(u'//div[@id="info"]//span[text()="编剧"]/following-sibling::a')]
        item['actors'] = [i.text for i in selector.xpath(u'//div[@id="info"]//span[text()="主演"]/following-sibling::a')]
        item['tags'] = [i.text for i in selector.xpath(u'//div[@id="info"]//span[text()="类型:"]/following-sibling::span[@property="v:genre"]')]
        item['official_website'] = selector.xpath(u'//div[@id="info"]//span[text()="官方网站:"]/following-sibling::a/@href')[0]
        item
        return info_list
