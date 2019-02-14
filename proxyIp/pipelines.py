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
        self.collection.insert_one(dict(item))
        return item
