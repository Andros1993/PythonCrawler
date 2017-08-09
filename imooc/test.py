# -*-coding:utf-8 -*-
from urllib import request

req = request.Request("https://www.amazon.ca/s/ref=nb_sb_noss_1/137-1949719-4324128?url=search-alias%3Daps&field-keywords=iphone")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

resp = request.urlopen(req)

print(resp.read().decode("utf-8"))