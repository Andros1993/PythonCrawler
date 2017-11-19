# -*-coding:utf-8 -*-
from urllib import request
import http.cookiejar
import time
import _thread
from bs4 import BeautifulSoup as bs
import re

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


def searchKeyworld(nextUrl, page, key_world, key_world_inde, ):
    htmlContent = init_url(nextUrl)

    # if page == 8:
    #     print(htmlContent)

    # print("正在搜索：" + str(page) + " 页")

    soup = bs(htmlContent, "html.parser")
    # li_list = soup.find_all('li', attrs={'class': 's-result-item  celwidget '})
    li_list = soup.find_all('li', attrs={'id': re.compile('result_')})
    # print("li_list len: " + str(len(li_list)))
    for text in li_list:
        asin = text.get('data-asin')
        if asin == 'B0771D5SSD':  # 护膝
            position = li_list.index(text) + 1
            if len(text.find_all(attrs={
                'class': "a-spacing-none a-color-tertiary s-sponsored-list-header s-sponsored-header sp-pixel-data a-text-normal"})) <= 0:
                # if len(text.find_all(attrs={'class' : 'a-declarative'})) <= 0:
                print(key_world + "搜索排名在第" + str(page) + "页" + "，第" + str(position) + "行")
                key_world_able_list[key_world_inde] = 0;
                break
            else:
                if key_world_able_list[key_world_inde] <= 0:
                    break
                print(key_world + "广告在第" + str(page) + "页" + "，第" + str(position) + "行")
                key_world_able_list[key_world_inde] -= 1;
                break


for key_world_str in key_world_list:

    print("正在搜索关键词：" + key_world_str)
    current_world_inde = key_world_list.index(key_world_str);
    # print(str(current_world_inde) + " : " + key_world_str)
    key_world_str = key_world_str.replace(" ", "+")
    base_url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dsporting&field-keywords=" + key_world_str
    htmlContent = init_url(base_url)

    _thread.start_new_thread(searchKeyworld, (base_url, 1, key_world_str, current_world_inde))

    index_start_string = htmlContent.find("/s/ref=sr_pg_2/")
    index_start = int(index_start_string)
    index_end_string = htmlContent.find("\"", index_start)
    index_end = int(index_end_string)
    pg2_undecode_url = htmlContent[index_start:index_end]
    pg2_undecode_url = pg2_undecode_url.replace(pg2_undecode_url[14: 34], "")

    for i in range(5):
        pg2_undecode_url = pg2_undecode_url.replace("&amp;", "&")

    for i in range(2, 400):
        time.sleep(2)
        # if the value is 0,then mean it fond 2 place of the key world, so dont need to do next anymore
        if key_world_able_list[current_world_inde] <= 0:
            break
        nextUrl = "https://www.amazon.com" + pg2_undecode_url.replace("/s/ref=sr_pg_2", "/s/ref=sr_pg_" + str(i))
        nextUrl = nextUrl.replace("page=2", "page=" + str(i))
        # print(nextUrl)
        try:
            _thread.start_new_thread(searchKeyworld, (nextUrl, i, key_world_str, current_world_inde,))
        except:
            print("Error: 无法启动线程")

    time.sleep(1)
