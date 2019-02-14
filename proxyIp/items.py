# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # ip
    ip = scrapy.Field()
    # 端口
    port = scrapy.Field()
    # 地区
    area = scrapy.Field()
    # 是否匿名
    anonymous = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 速度
    speed = scrapy.Field()
    # 连接时间
    connection_time = scrapy.Field()
