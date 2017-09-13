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
        # print('title:' + str(new_li_list.index(lin_text)))
        title = lin_text.find_all(attrs={'class': 'a-size-medium s-inline s-access-title a-text-normal'})[0].attrs['data-attribute']
        table.write(new_li_list.index(lin_text), 0, title)

    # 获取链接的品牌
    for lin_text in new_li_list:
        brand = lin_text.find_all(attrs={'class': 'a-row a-spacing-small'})[0].find_all(attrs={'class': 'a-row a-spacing-none'})[0].find_all(attrs={'class': 'a-size-small a-color-secondary'})[1].string
        table.write(new_li_list.index(lin_text), 1, brand)

    # 获取价格
    for lin_text in new_li_list:
        large_price = lin_text.find_all(attrs={'class': 'sx-price sx-price-large'})
        # print('price:' + str(new_li_list.index(lin_text)))
        if len(large_price) == 0:
            price = "自发货价格：" + lin_text.find_all(attrs={'class': 'a-size-base a-color-base'})[0].string
            table.write(new_li_list.index(lin_text), 2, price)
        else:
            price = large_price[0].find("span").string + '.' + large_price[0].find_all("sup")[1].string
            table.write(new_li_list.index(lin_text), 2, price)

    # 获取reiew数量
    for lin_text in new_li_list:
        review = lin_text.find_all(attrs={'class': 'a-column a-span5 a-span-last'})[0].find_all(attrs={'class': 'a-size-small a-link-normal a-text-normal'})[0].string
        table.write(new_li_list.index(lin_text), 3, review)

    # 获取review等级
    for lin_text in new_li_list:
        review_level = lin_text.find_all(attrs={'class': 'a-popover-trigger a-declarative'})[0].find_all(attrs={'class': 'a-icon-alt'})[0].string[0:3]
        if review_level.find('o') == -1:
            table.write(new_li_list.index(lin_text), 4, review_level)
        else:
            table.write(new_li_list.index(lin_text), 4, review_level[0:1] + '.0')

    # 获取上架时间
    for lin_text in new_li_list:

        # 进入review界面
        detail_href = lin_text.find_all(attrs={'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})[0].attrs['href']
        detail_html_content = get_rul_conten(detail_href)
        detail_soup = bs(detail_html_content, "html.parser")
        # 进入所有review界面
        see_all_href = 'https://www.amazon.com' + detail_soup.find_all(attrs={'class': 'a-link-emphasis a-text-bold'})[0].attrs['href']
        # print("所有页面链接：" + see_all_href)
        see_all_html_content = get_rul_conten(see_all_href)
        see_all_soup = bs(see_all_html_content, "html.parser")
        page_list = see_all_soup.find_all(attrs={'class': 'a-text-center celwidget a-text-base'})[0].find_all(attrs={'class': 'page-button'})
        # 进入最后一页review界面
        last_page_href = 'https://www.amazon.com' + page_list[len(page_list) - 1].a.attrs['href']
        # print("最后一页review链接：" + last_page_href)
        last_page_html_content = get_rul_conten(last_page_href)
        last_page_soup = bs(last_page_html_content, "html.parser")
        last_page_review_list = last_page_soup.find_all(attrs={'id': 'cm_cr-review_list'})[0].find_all(attrs={'class': 'a-section review'})
        upload_date = last_page_review_list[len(last_page_review_list) - 1].find_all(attrs={'class': 'a-size-base a-color-secondary review-date'})[0].string
        # print(last_page_review_list[len(last_page_review_list) - 1].find_all(attrs={'class': 'a-size-base a-color-secondary review-date'})[0].string)
        table.write(new_li_list.index(lin_text), 5, upload_date[3:])
        time.sleep(1)

    # 保存文件
    file.save('file.xls')

base_url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=knee+brace"
htmlContent = get_rul_conten(base_url)
get_first_page_all_list(htmlContent)
