# proxyIp
> proxyIp基于scrapy框架编写，利用MongoDB进行存储
- 安装MongoDB
- 安装依赖`pip install -r requirements.txt`
- 开始爬虫`scrapy crawl xici`
- IP代理池维护 `python checkIp.py`，建议写一个定时任务，每隔一个小时跑一次

### 更新日志
- v1.0 仅支持爬西刺
- v1.1 支持ip查重过滤
- v2.0 IP代理池维护
- v2.1 优化日志
