# -*- coding: utf-8 -*-
import scrapy
from firstblood.items import FirstbloodItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']

    url = 'https://www.qiushibaike.com/8hr/page/{}/'
    page = 1

    def parse(self, response):
        div_list = response.xpath("//div[@id='content-left']/div")

        for odiv in div_list:
            item = FirstbloodItem()

            face = odiv.xpath('./div[@class="author clearfix"]//img/@src').extract_first()            
            name = odiv.xpath('./div[@class="author clearfix"]//h2/text()').extract_first()
            age = odiv.xpath('./div[@class="author clearfix"]//div/text()').extract_first()
            content = odiv.xpath('.//div[@class="content"]/span/text()').extract_first()
            haha_count = odiv.xpath('.//div[@class="stats"]/span[1]//i/text()').extract_first()
            ping_count = odiv.xpath('.//div[@class="stats"]/span[2]//i/text()').extract_first()
            face = 'https:' + face
            name = name.strip('\n')
            content = content.strip('\n')
            # item = {
            #     '头像':face,
            #     '用户名':name,
            #     '用户年龄':age,
            #     '内容':content,
            #     '好笑个数':haha_count,
            #     '评论个数':ping_count,
            # }
            # print('*' *50)
            # print(item)
            # print('*' *50)
            item['face'] = face
            item['name'] = name
            item['age'] = age
            item['content'] = content
            item['haha_count'] = haha_count
            item['ping_count'] = ping_count

            yield item
        # 上面执行完后进行判断，然后回调
        if self.page <= 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url,callback=self.parse)
