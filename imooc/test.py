# -*-coding:utf-8 -*-
from urllib import request

# # req = request.Request("https://www.amazon.ca/s/ref=sr_pg_2/138-4822442-6956431?fst=as%3Aon&amp;rh=n%3A667823011%2Ck%3Aiphone&amp;page=2&amp;keywords=iphone&amp;ie=UTF8&amp;qid=1502342373&amp;spIA=B072VHT174,B072JCTC8D,B072VGMCW1")
# # req = request.Request("https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone")
# req = request.Request("https://www.amazon.ca")
# # req = request.Request("https://www.baidu.com")
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
# req.add_header("Host","www.amazon.ca")
# # req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
# # req.add_header("Accept-Encoding","gzip, deflate, sdch, br")
# req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
# req.add_header("Host","www.amazon.ca")
# req.add_header("Upgrade-Insecure-Requests","1")
# req.add_header("Connection","keep-alive")
# req.add_header("Cache-Control","max-age=0")
# # req.add_header("Cookie","x-wl-uid=1qJZtXvZqdhGo6WrKG7RWxDBH2VNJNQ3I2JCpgAFphTfQugGUxfFQMXiO3IHp9MoHd10aocEowq8=; session-token=2wQbtOT0dMHq/GUXVphqVBIaaPx9YOaoPBJjuJpDLKy71PaY8iRz700ZRlu7Qzq+wkAs6uwA1D/YMsA6dKu6vEL7rZkVOBtAjxOyGQWy1tCPvmqUqKCWiL2Qw85X2dvm8qujRMLPVq8OaF42kBEeHc1OcGIaeIldydPUEicrN1BHVz2mairqeioXxsaO2m/3MbVeajUzVfNmJwc6O0qEn5I0GYSO+MQAs3A0pY5M7eOl/ex+YRKeETFHisFLvWIb; JSESSIONID=D125BF86621F47C850170F86BCA4B3D8; csm-hit=s-7WA8RC56R24R1YG5A5SZ|1502342013259; session-id-time=2082787201l; session-id=137-1949719-4324128; ubid-acbca=131-5460029-5255764")
#
# resp = request.urlopen(req)
#
# print(resp.read().decode("utf-8"))
print("---------------------------------fire line-----------------------------------")

req = request.Request("https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "iphone")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
req.add_header("Host","www.amazon.ca")
req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
req.add_header("Host","www.amazon.ca")
req.add_header("Upgrade-Insecure-Requests","1")
req.add_header("Connection","keep-alive")
req.add_header("Cache-Control","max-age=0")

resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
