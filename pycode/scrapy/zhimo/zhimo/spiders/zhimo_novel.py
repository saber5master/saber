# -*- coding: utf-8 -*-
import scrapy
from zhimo.items import ZhimoItem
import time

class ZhimoNovelSpider(scrapy.Spider):
    name = 'zhimo_novel'
    allowed_domains = ['woquge.com']
    start_urls = ['http://www.woquge.com/0_30/']

    def parse(self, response):
        novel_links = response.xpath('//dd/a/@href').extract()
        for url in novel_links:
            if type(url) == str:
                time.sleep(5)
                yield scrapy.Request(url, callback = self.next_parse)
            else:
                continue

    def next_parse(self, response):
        item = ZhimoItem()
        item['novel_head'] = response.xpath('//h1/text()').extract()
        print(item['novel_head'])
        item['novel_text'] = response.xpath('//p/text()').extract()
        yield item


