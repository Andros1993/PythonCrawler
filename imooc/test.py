# -*-coding:utf-8 -*-
from urllib import request

resp = request.urlopen("http://www.baidu.com")
resp.add_header()

print(resp.read().decode("utf-8"))