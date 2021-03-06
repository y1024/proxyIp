# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from pymongo import MongoClient
import sys
import codecs
from setLogger import Logger


class CheckIp:
    def __init__(self):
        client = MongoClient()
        db = client.ips
        self.collection = db.list
        self.logger = Logger("checkIp.log")

    def check_ip(self, type, ip, port):
        ua = UserAgent()
        headers = ua.random
        self.logger.info("正在检测：%s" % ip)
        try:
            request = requests.get("https://www.baidu.com", headers={'user-agent': headers},
                                   proxies={'http': "%s://%s:%s" % (type, ip, port)}, timeout=2)
            if request.status_code != 200:
                self.logger.info("请求失败，状态码：%d" % request.status_code)
                return True
            else:
                self.logger.info("请求成功，状态码：%d" % request.status_code)
                return False
        except:
            self.logger.warning("请求异常")
            return True

    def get_ips(self):
        del_count = 0
        ip_list = self.collection.find()
        ip_count = ip_list.count()
        if ip_count > 0:
            self.logger.info("过滤开始")
            for item in list(ip_list):
                result = self.check_ip(item['type'].lower(), item['ip'], item['port'])
                if result:
                    self.logger.info("正在清除")
                    self.collection.remove({'ip': item['ip']})
                    del_count = del_count + 1
                    self.logger.info("已清除")
        else:
            self.logger.info("无数据")
        self.logger.info("过滤IP结束,过滤总数：%d个,共清除：%d个" % (ip_count, del_count))


if __name__ == '__main__':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    checkIp = CheckIp()
    checkIp.get_ips()
