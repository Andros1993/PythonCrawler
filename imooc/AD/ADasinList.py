# -*-coding:utf-8 -*-
from urllib import request
import time
import _thread
from bs4 import BeautifulSoup as bs
import re
import http.cookiejar
import xlrd
import xlwt
import random

rowCount = 0

key_world_list = [
    #     "knee brace",
    # "knee support",
    # "knee sleeve",
    # "knee compression sleeve",
    # "knee",
    # "knee compression",
    # "compression knee brace",
    "knee brace",

    "knee compression sleeve",
    "knee support",
    "knee brace",
"for meniscus tear",
"knee brace for man",
"knee brace for women",
"knee brace for men",
"knee brace for arthritis",
"knee sleeve",
];
key_world_able_list = [
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
]


def init_url(url):
    cookie = http.cookiejar.LWPCookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cookie))
    request.install_opener(opener)
    # response3 = request.urlopen("https://www.amazon.com")
    req = request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    req.add_header("Host", "www.amazon.com")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("Host", "www.amazon.com")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")

    resp = request.urlopen(req)
    htmlContentBuf = resp.read().decode('utf-8')
    resp.close()
    return htmlContentBuf


def getTheAdAsin(nextUrl, page, key_world, key_world_inde, table, ):
    htmlContent = init_url(nextUrl)

    soup = bs(htmlContent, "html.parser")

    indexCount = 0;

    # 获取所有搜索结果
    li_list = soup.find_all('li', attrs={'id': re.compile('result_')})
    for text in li_list:
        # 获取属于广告的结果
        h5_list = text.find_all('h5', attrs={'class': re.compile('a-spacing-none a-color-tertiary s-sponsored-list-header s-sponsored-header sp-pixel-data a-text-normal')})
        if len(h5_list) >0 :
            asin = text.get('data-asin')
            if asin == "B0771D5SSD" :
                table.write(rowCount, 0, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                table.write(rowCount, 1, page)
                table.write(rowCount, 2, indexCount)
                indexCount = indexCount + 1
                rowCount = rowCount + 1
                file.release_resources()

if __name__ == "__main__":

    # 新建一个excel文件
    file = xlwt.Workbook.
    # 新建一个sheet
    table = file.sheet_by_name('Sheet1')
    # 写入数据table.write(行,列,value)
    # table.write(0, 0, 'wangpeng')
    # file.save('knee+support.xls')

    table.cell()
    table.write(0, 0, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    while False:
        for key_world_str in key_world_list:

            print("正在搜索关键词：" + key_world_str)
            current_world_inde = key_world_list.index(key_world_str);
            # print(str(current_world_inde) + " : " + key_world_str)
            key_world_str = key_world_str.replace(" ", "+")
            base_url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + key_world_str
            htmlContent = init_url(base_url)

            _thread.start_new_thread(getTheAdAsin, (base_url, 1, key_world_str, current_world_inde, table))

            index_start_string = htmlContent.find("/s/ref=sr_pg_2/")
            index_start = int(index_start_string)
            index_end_string = htmlContent.find("\"", index_start)
            index_end = int(index_end_string)
            pg2_undecode_url = htmlContent[index_start:index_end]
            pg2_undecode_url = pg2_undecode_url.replace(pg2_undecode_url[14: 34], "")

            for i in range(5):
                pg2_undecode_url = pg2_undecode_url.replace("&amp;", "&")

            for i in range(2, 10):
                time.sleep(3 + random.randint(0,4))
                # if the value is 0,then mean it fond 2 place of the key world, so dont need to do next anymore
                if key_world_able_list[current_world_inde] <= 0:
                    break
                nextUrl = "https://www.amazon.com" + pg2_undecode_url.replace("/s/ref=sr_pg_2", "/s/ref=sr_pg_" + str(i))
                nextUrl = nextUrl.replace("page=2", "page=" + str(i))
                # print(nextUrl)
                try:
                    _thread.start_new_thread(getTheAdAsin, (nextUrl, i, key_world_str, current_world_inde, table,))
                except:
                    print("Error: 无法启动线程")

            time.sleep(random.randint(0,4))
        time.sleep(360 + random.randint(0,9))
