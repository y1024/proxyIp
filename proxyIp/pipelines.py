# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class ProxyipPipeline(object):
    def __init__(self):
        client = MongoClient()
        db = client.ips
        self.collection = db.list

    def process_item(self, item, spider):
        item = dict(item)
        # 检测ip是否存在
        exist = self.collection.find_one({'ip': item['ip']})
        if exist:
            print("%s已存在" % item['ip'])
        else:
            self.collection.insert_one(item)
        return item
