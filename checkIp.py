import requests
from fake_useragent import UserAgent
from pymongo import MongoClient


class CheckIp:
    def __init__(self):
        client = MongoClient()
        db = client.ips
        self.collection = db.list

    def check_ip(self, proxy):
        ua = UserAgent()
        headers = ua.random
        request = requests.get("https://www.baidu.com", headers=headers, proxy={proxy})
        if request.status_code != 200:
            return True
        else:
            return False

    def get_ips(self):
        ip_list = self.collection.find()
        if ip_list.count() > 0:
            for item in list(ip_list):
                proxy = "%s://%s:%s" % (item['type'], item['ip'], item['port'])
                result = self.check_ip(proxy)
                if result:
                    self.collection.remove({'ip': item['ip']})


checkIp = CheckIp()
checkIp.get_ips()
