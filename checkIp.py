# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from pymongo import MongoClient
import sys
import codecs
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%Y-%d-%m %H:%M:%S',
                    filename='/data/log/checkIp.log', filemode='w', level=logging.DEBUG)


class CheckIp:
    def __init__(self):
        client = MongoClient()
        db = client.ips
        self.collection = db.list

    def check_ip(self, type, ip, port):
        ua = UserAgent()
        headers = ua.random
        logging.info("正在检测：%s" % ip)
        try:
            request = requests.get("https://www.baidu.com", headers={'user-agent': headers},
                                   proxies={'http': "%s://%s:%s" % (type, ip, port)}, timeout=2)
            if request.status_code != 200:
                logging.info("请求失败，状态码：%d" % request.status_code)
                return True
            else:
                logging.info("请求成功，状态码：%d" % request.status_code)
                return False
        except:
            logging.warning("请求异常")
            return True

    def get_ips(self):
        del_count = 0
        ip_list = self.collection.find()
        if ip_list.count() > 0:
            logging.info("过滤开始")
            for item in list(ip_list):
                result = self.check_ip(item['type'].lower(), item['ip'], item['port'])
                if result:
                    logging.info("正在清除")
                    self.collection.remove({'ip': item['ip']})
                    del_count = del_count + 1
                    logging.info("已清除")
        else:
            logging.info("无数据")
        logging.info("过滤结束,共清除：%d个IP" % del_count)


if __name__ == '__main__':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    checkIp = CheckIp()
    checkIp.get_ips()
