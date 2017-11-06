from urllib import request
import time
import _thread
from bs4 import BeautifulSoup as bs
import re


def init_url(url):
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36")
    req.add_header("Host", "www.baidu.com")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("Host", "www.baidu.com")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")

    resp = request.urlopen(req)
    htmlContentBuf = resp.read().decode('utf-8')
    return htmlContentBuf;


htmlContent = init_url("https://baidu.com")
# chrome 抓取的百度访问链接
# https://www.baidu.com/s?wd=注册&rsv_spt=1&rsv_iqid=0x901d428300023f55&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=%25E6%25B3%25A8%25E5%2586%258C&rsv_t=4dcckzUHOeaJ5jElK7QQxLYFT4GXAPxLQxvSaB2YGIwA0bM27EiTnqK%2BmX6e59OgqmLk&rsv_pq=b1e81d7800028610&rsv_sug=1
print(htmlContent)