# -*-coding:utf-8 -*-
from urllib import request
import time

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
# print("---------------------------------fire line-----------------------------------")

# test data
# s/ref=sr_pg_2/135-8934197-1228839?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=2&keywords=iphone&ie=UTF8&qid=1502631714&spIA=B072FQC5RR,B071F1BMRM,B019X7KM3A

# real data
# /s/ref=sr_pg_2?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=2&keywords=iphone&ie=UTF8&qid=1502635386&spIA=B072FQC5RR,B07435M7FF,B071F1BMRM
# /gp/search/ref=sr_pg_3?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=3&keywords=iphone&ie=UTF8&qid=1502635488&spIA=B072FQC5RR,B07435M7FF,B071F1BMRM,B072VFHKH5,B071NSF8M3,B019X7KM3A
# /gp/search/ref=sr_pg_4?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=4&keywords=iphone&ie=UTF8&qid=1502635624&spIA=B072FQC5RR,B07435M7FF,B071F1BMRM,B072VFHKH5,B071NSF8M3,B019X7KM3A,B01N0ZTKJ0,B07282BVKY,B0731N7T7L
# /gp/search/ref=sr_pg_5?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=5&keywords=iphone&ie=UTF8&qid=1502635719&spIA=B072FQC5RR,B07435M7FF,B071F1BMRM,B072VFHKH5,B071NSF8M3,B019X7KM3A,B01N0ZTKJ0,B07282BVKY,B0731N7T7L,B06XNNY8X9,B072VD99RM,B0732QXFBZ

# /s/ref=sr_pg_3?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=3&keywords=iphone&ie=UTF8&qid=1502802229&spIA=B072FQC5RR,B07282BVKY,B072VFHKH5,B01N0ZTKJ0,B0732QXFBZ,B06XNNY8X9
# /gp/search/ref=sr_pg_4?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=4&keywords=iphone&ie=UTF8&qid=1502802364&spIA=B072FQC5RR,B07282BVKY,B072VFHKH5,B01N0ZTKJ0,B0732QXFBZ,B06XNNY8X9,B0714NB918,B071F1BMRM,B072KSDPQN
# /s/ref=sr_pg_5?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=5&keywords=iphone&ie=UTF8&qid=1502802394&spIA=B072FQC5RR,B07282BVKY,B072VFHKH5,B01N0ZTKJ0,B0732QXFBZ,B06XNNY8X9,B0714NB918,B071F1BMRM,B072KSDPQN,B017CRMIV2,B01N7ZG7DJ,B0731LTYYT
# /gp/search/ref=sr_pg_6?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=6&keywords=iphone&ie=UTF8&qid=1502802450&spIA=B072FQC5RR,B07282BVKY,B072VFHKH5,B01N0ZTKJ0,B0732QXFBZ,B06XNNY8X9,B0714NB918,B071F1BMRM,B072KSDPQN,B017CRMIV2,B01N7ZG7DJ,B0731LTYYT,B06XN6M3Z7,B01AYY840Y,B072WMYX6D
# /gp/search/ref=sr_pg_7?fst=as%3Aon&rh=n%3A667823011%2Ck%3Aiphone&page=7&keywords=iphone&ie=UTF8&qid=1502802934&spIA=B072FQC5RR,B07282BVKY,B072VFHKH5,B01N0ZTKJ0,B0732QXFBZ,B06XNNY8X9,B0714NB918,B071F1BMRM,B072KSDPQN,B017CRMIV2,B01N7ZG7DJ,B0731LTYYT,B06XN6M3Z7,B01AYY840Y,B072WMYX6D,B072VD99RM,B00SSM6L4Q,B071NSF8M3



# req = request.Request("https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "iphone")
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
# req.add_header("Host","www.amazon.ca")
# req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
# req.add_header("Host","www.amazon.ca")
# req.add_header("Upgrade-Insecure-Requests","1")
# req.add_header("Connection","keep-alive")
# req.add_header("Cache-Control","max-age=0")
#
# resp = request.urlopen(req)
#
# htmlContent = resp.read().decode('utf-8')
def init_url(url):
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    req.add_header("Host", "www.amazon.ca")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("Host", "www.amazon.ca")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")

    resp = request.urlopen(req)
    htmlContentBuf = resp.read().decode('utf-8')
    return htmlContentBuf;


# backup####################################################################################################
# htmlContent = init_url("https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "fm+transmitter")
#
# # handle data
# index_start_string = htmlContent.find("/s/ref=sr_pg_2/")
# index_start = int(index_start_string)
# index_end_string = htmlContent.find("\"",index_start)
# index_end = int(index_end_string)
# pg2_undecode_url = htmlContent[index_start:index_end]
#
# pg2_undecode_url = pg2_undecode_url.replace(pg2_undecode_url[14 : 34],"")
#
# for i in range(5):
#     pg2_undecode_url = pg2_undecode_url.replace("&amp;","&")
#
# htmlcontent2 = init_url("https://www.amazon.ca" + pg2_undecode_url)
#
# getResult = htmlcontent2.find("Bluetooth FM Transmitter,[Newest Version]Etybetopstar T11 Car Transmitter Radio Adapter Car Kit with 4 Music Play Mode/Hands-Free Calling/1.44 Inch Screen Display/USB Car Charger/Support TF Card/U Disk/AUX Input for Mobile Audio Devices,Black")
#
# print(htmlcontent2)
# if getResult != -1:
#     print("找到了，在第2页")
# print(pg2_undecode_url)

htmlContent = init_url("https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + "fm+transmitter")

# handle data
for i in range(2,100):

    getResult = htmlContent.find("Bluetooth FM Transmitter,[Newest Version]Etybetopstar T11 Car Transmitter Radio Adapter Car Kit with 4 Music Play Mode/Hands-Free Calling/1.44 Inch Screen Display/USB Car Charger/Support TF Card/U Disk/AUX Input for Mobile Audio Devices,Black")

    if getResult != -1:
        print("找到了，在第2页")

    index_start_string = htmlContent.find("/s/ref=sr_pg_" + str(i) + "/")
    index_start = int(index_start_string)
    index_end_string = htmlContent.find("\"",index_start)
    index_end = int(index_end_string)
    pg2_undecode_url = htmlContent[index_start:index_end]

    pg2_undecode_url = pg2_undecode_url.replace(pg2_undecode_url[14 : 34],"")

    for i in range(5):
        pg2_undecode_url = pg2_undecode_url.replace("&amp;","&")

    print(pg2_undecode_url)
    htmlContent = init_url("https://www.amazon.ca" + pg2_undecode_url)
    time.sleep(3)



