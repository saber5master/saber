# -*- coding: utf-8 -*-
import scrapy
from july.items import JulyItem

class JulyClassSpider(scrapy.Spider):
    name = 'july_class'
    allowed_domains = ['julyedu.com']
    start_urls = ['https://www.julyedu.com/video/index']

    def parse(self, response):
        info_list = response.xpath("//div[@class = 'course_info_box']")
        for info in info_list:
            item = JulyItem()
            item["class_name"] = info.xpath("./a/h4").extract()[0]
            item["class_tag"] = info.xpath("./a/p[1]").extract()[0]
            item["study_num"] = info.xpath("./a/p[2]/span[2]").extract()[0]
            item["class_link"] = "http://www.julyedu.com" + info.xpath("./a/@href").extract()[0]
            yield item
            


