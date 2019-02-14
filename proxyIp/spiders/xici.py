# -*- coding: utf-8 -*-
import scrapy
from proxyIp.items import ProxyipItem


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/wn/',
                  'https://www.xicidaili.com/wt/']

    def parse(self, response):
        print("请求成功:%s" % response.request.url)
        ul = response.css('#ip_list')
        for li in ul:
            tr = li.css('tr:nth-child(n+2)')
            for td in tr:
                item = ProxyipItem()
                # 国家
                item['country'] = td.css('td:nth-child(1) img::attr(alt)').extract_first()
                # ip
                item['ip'] = td.css('td:nth-child(2)::text').extract_first()
                # 端口
                item['port'] = td.css('td:nth-child(3)::text').extract_first()
                # 地区
                item['area'] = td.css('td:nth-child(4) a::text').extract_first()
                # 是否匿名
                item['anonymous'] = td.css('td:nth-child(5)::text').extract_first()
                # 类型
                item['type'] = td.css('td:nth-child(6)::text').extract_first()
                # 速度
                item['speed'] = td.css('td:nth-child(7) div::attr(title)').extract_first()
                # 连接时间
                item['connection_time'] = td.css('td:nth-child(8) div::attr(title)').extract_first()
                yield item
        page_href = response.css('.next_page::attr(href)').extract_first()
        page_num = int(response.css('.pagination em.current::text').extract_first())
        print("爬取完成:%s" % response.request.url)
        if page_num < 5:
            yield response.follow(page_href, callback=self.parse)
