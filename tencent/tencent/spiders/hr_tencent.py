# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class HrTencentSpider(scrapy.Spider):
    name = 'hr_tencent'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']")

        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = node.xpath("./td[1]/a/@href").extract()[0]
            if len(node.xpath("./td[2]/text()")):
                item['position_type'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['position_type'] = ""
            item['people_number'] = node.xpath("./td[3]/text()").extract()[0]
            item['work_address'] = node.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = node.xpath("./td[5]/text()").extract()[0]
            print(item['publish_time'])
            yield item

            if self.offset < 20:
                self.offset += 10
                url = self.base_url + str(self.offset)
                yield scrapy.Request(url, callback = self.parse)

