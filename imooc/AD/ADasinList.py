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

head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                   'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                   'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                   'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                   'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                   'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

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
    # cookie = http.cookiejar.LWPCookieJar()
    # opener = request.build_opener(request.HTTPCookieProcessor(cookie))
    # request.install_opener(opener)
    # response3 = request.urlopen("https://www.amazon.com")
    req = request.Request(url)
    req.add_header("User-Agent",
                   head_user_agent[random.randint(0,18)])
    req.add_header("Host", "www.amazon.com")
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
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
    print(nextUrl)
    htmlContent = init_url(nextUrl)

    soup = bs(htmlContent, "html.parser")

    indexCount = 0;

    # 获取所有搜索结果
    li_list = soup.find_all('li', attrs={'id': re.compile('result_')})
    print("第" + str(page) + "页" + str(len(li_list)))
    for text in li_list:
        # 获取属于广告的结果
        h5_list = text.find_all('h5', attrs={'class': re.compile('a-spacing-none a-color-tertiary s-sponsored-list-header s-sponsored-header sp-pixel-data a-text-normal')})
        if len(h5_list) >0 :
            indexCount = indexCount + 1;
            asin = text.get('data-asin')
            # if asin == "B073R7TK7N" :
                # print(str(page) + " 页 " + " 第 " + str(indexCount) + "个")
            print(asin)
            # table.write(rowCount, 0, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            # table.write(rowCount, 1, page)
            # table.write(rowCount, 2, indexCount)
            # indexCount = indexCount + 1
            # rowCount = rowCount + 1
            # file.release_resources()
    soup.reset()

if __name__ == "__main__":

    # 新建一个excel文件
    file = xlrd.open_workbook("us_knee_brace_ad.xlsx")
    # 新建一个sheet
    table = file.sheet_by_name('Sheet1')
    # 写入数据table.write(行,列,value)
    # table.write(0, 0, 'wangpeng')
    # file.save('knee+support.xls')

    # table.cell()
    # table.write(0, 0, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    while True:
        for key_world_str in key_world_list:

            print("正在搜索关键词：" + key_world_str)
            current_world_inde = key_world_list.index(key_world_str);
            # print(str(current_world_inde) + " : " + key_world_str)
            key_world_str = key_world_str.replace(" ", "+")
            base_url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + key_world_str
            htmlContent = init_url(base_url)

            # _thread.start_new_thread(getTheAdAsin, (base_url, 1, key_world_str, current_world_inde, table))
            getTheAdAsin(base_url, 1, key_world_str, current_world_inde, table)

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

                # index_begin_string = nextUrl.find("&qid=")
                # index_begin = int(index_begin_string)
                #
                # nextUrl = nextUrl.replace(nextUrl[index_begin : len(nextUrl)], "")
                # print(nextUrl)
                # try:
                #     _thread.start_new_thread(getTheAdAsin, (nextUrl, i, key_world_str, current_world_inde, table,))
                # except:
                #     print("Error: 无法启动线程")
                getTheAdAsin(nextUrl, i, key_world_str, current_world_inde, table)

            time.sleep(random.randint(0,4))
        time.sleep(360 + random.randint(0,9))
