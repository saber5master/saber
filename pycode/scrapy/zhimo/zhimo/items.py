# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhimoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_head = scrapy.Field() #小说题目
    novel_text = scrapy.Field() #小说文本

