# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class FirstbloodPipeline(object):
    def open_spider(self,spider):
        self.fp = open('qiubai.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        dic = dict(item)
        # 将字典转为json格式
        string = json.dumps(dic,ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self,spider):
        self.fp.close()