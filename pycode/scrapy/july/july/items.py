# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JulyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # //div[@class = 'course_info_box']
    # 课程名称
    class_name = scrapy.Field()
    # 课程标签
    class_tag = scrapy.Field()
    # 学习人数
    study_num = scrapy.Field()
    # 课程链接
    class_link = scrapy.Field()

