# -*-coding:utf-8 -*-
from urllib import request
import time
import _thread
from bs4 import BeautifulSoup as bs

#           "fm transmitter",
#     		"car bluetooth fm transmitter",
#     		"car fm transmitter bluetooth",
#     		"fm transmitter for car bluetooth",
#     		"fm transmitter for phone",
#     		"car bluetooth fm",
#     		"bluetooth usb transmitter",
#     		"fm transmitter charger",
#     		"fm transmitter car charger",
#     		"fm transmitter kit",
#     		"fm transmitter car kit",
#     		"car fm transmitter usb",
#     		"fm transmitter hands free",
#     		"bluetooth fm transmitter car kit"

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

def searchKeyworld(nextUrl, page):
    htmlContent = init_url(nextUrl)
    soup = bs(htmlContent, "html.parser")
    liList = soup.find_all('li')
    for text in soup.find_all('li'):
        asin = text.get('data-asin')
        if asin == 'B072KCY51R':
            position = liList.index(text)
            if position % 3 == 0:
                row_position = position / 3
                list_position = 3
            else:
                row_position = (position / 3) + 1
                list_position = position % 3

            print("找到了，在第" + str(page) + "页，" + "，第" + str(row_position) + "行" + ",第" + str(list_position) + "个")
            print(position)

htmlContent = init_url("https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Delectronics&field-keywords=" + "fm+transmitter" + "&rh=n%3A667823011%2Ck%3A" + "fm+transmitter")
getResult = htmlContent.find("Perbeat BT66 Wireless Bluetooth FM Transmitter Hands free Car Kit Radio Adapter MP3 Player Dual USB Car Charger support Micro SD Card USB Flash Disk for Smart phone, iPhone, iPad,etc (Blue)")#"Bluetooth FM Transmitter,[Newest Version]Etybetopstar T11 Car Transmitter Radio Adapter Car Kit with 4 Music Play Mode/Hands-Free Calling/1.44 Inch Screen Display/USB Car Charger/Support TF Card/U Disk/AUX Input for Mobile Audio Devices,Black")

if getResult != -1:
    print("找到了，在第1页")

index_start_string = htmlContent.find("/s/ref=sr_pg_2/")
index_start = int(index_start_string)
index_end_string = htmlContent.find("\"",index_start)
index_end = int(index_end_string)
pg2_undecode_url = htmlContent[index_start:index_end]
pg2_undecode_url = pg2_undecode_url.replace(pg2_undecode_url[14 : 34],"")

for i in range(5):
    pg2_undecode_url = pg2_undecode_url.replace("&amp;","&")

for i in range(3,50):

    nextUrl = "https://www.amazon.ca" + pg2_undecode_url.replace("/s/ref=sr_pg_2", "/s/ref=sr_pg_" + str(i))
    nextUrl = nextUrl.replace("page=2", "page=" + str(i))
    try:
        _thread.start_new_thread(searchKeyworld, (nextUrl, i,))
    except:
        print("Error: 无法启动线程")
    time.sleep(0.8)
