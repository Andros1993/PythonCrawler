# -*-coding:utf-8 -*-
from urllib import request
import time
import _thread
from bs4 import BeautifulSoup as bs
import re
import xlrd
import xlwt

def get_rul_conten(url):
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    req.add_header("Host", "www.amazon.com")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("Host", "www.amazon.com")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")

    resp = request.urlopen(req)
    htmlContentBuf = resp.read().decode('utf-8')
    return htmlContentBuf;

# def handle_lin_text(lin_text):


def get_first_page_all_list(htmlContent):
    soup = bs(htmlContent, "html.parser")
    li_list = soup.find_all('li', attrs={'id': re.compile('result_')})
    # 新建一个excel文件
    file = xlwt.Workbook()
    # 新建一个sheet
    table = file.add_sheet('info', cell_overwrite_ok=True)
    # 写入数据table.write(行,列,value)
    # table.write(0, 0, 'wangpeng')


    # 删除所有广告链接
    count = 0;
    new_li_list = []
    while count < len(li_list):
        if str(li_list[count]).find("Sponsored") == -1:
            new_li_list.append(li_list[count])
        count = count + 1
    # for lin_text in li_list:
    #     print(lin_text)
    #     if lin_text.find("a-spacing-none a-color-tertiary s-sponsored-list-header a-text-normal") != -1:
    #         li_list.remove(lin_text)
    # 处理所有有效的链接----------------------------

    # 获取链接的title
    for lin_text in new_li_list:
        title = lin_text.find_all(attrs={'class': 'a-size-medium s-inline s-access-title a-text-normal'})[0].attrs['data-attribute']
        table.write(new_li_list.index(lin_text), 0, title)

    # 获取链接的品牌
    for lin_text in new_li_list:
        brand = lin_text.find_all(attrs={'class': 'a-row a-spacing-small'})[0].find_all(attrs={'class': 'a-row a-spacing-none'})[0].find_all(attrs={'class': 'a-size-small a-color-secondary'})[1].string
        table.write(new_li_list.index(lin_text), 1, brand)

    # 获取价格
    for lin_text in new_li_list:
        large_price = lin_text.find_all(attrs={'class': 'sx-price sx-price-large'})
        if len(large_price) == 0:
            price = "自发货价格：" + lin_text.find_all(attrs={'class': 'a-size-base a-color-base'})[0].string
            table.write(new_li_list.index(lin_text), 2, price)
        else:
            price = large_price[0].find("span").string + '.' + large_price[0].find_all("sup")[1].string
            table.write(new_li_list.index(lin_text), 2, price)

    # 保存文件
    file.save('file.xls')

base_url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=knee+brace"
htmlContent = get_rul_conten(base_url)
get_first_page_all_list(htmlContent)
