# -*-coding:utf-8 -*-
import random
import threading
from urllib import request
import time
import _thread

import xlwt
from bs4 import BeautifulSoup as bs
import re
import xlrd;
#import xlutils;
from xlutils.copy import copy;


def init_url(url):
    req = request.Request(url)
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36")
    req.add_header("Host", "www.feixiaohao.com")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
    # req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("If-Modified-Since", "Mon, 04 Jun 2018 14:08:54 GMT")
    # req.add_header("Accept-Encoding", "gzip, deflate, br")
    req.add_header("Cookie", "usid=bf81e7efe5f65396; UM_distinctid=163cb1691911be-0db5ca4e4aac54-3b60490d-1fa400-163cb16919212b; CNZZDATA1263003344=408349772-1528120479-https%253A%252F%252Fwww.baidu.com%252F%7C1528120479; Hm_lvt_192e611c7ffa4b2f8a5047e5cf45403f=1528120645; Hm_lpvt_192e611c7ffa4b2f8a5047e5cf45403f=1528121371")

    try :
        resp = request.urlopen(req)
        htmlContentBuf = resp.read().decode('utf-8')
        return htmlContentBuf;
    except BaseException:
        return ""

# # 新建一个excel文件
# file = xlwt.Workbook()
# # 新建一个sheet
# table = file.add_sheet('info', cell_overwrite_ok=True)
#
rowCount = 0;

# def searchEmail(infoUrl):
#     rvInfoContent = init_url("https://www.feixiaohao.com/" + infoUrl)
#     # if rvInfoContent.find("\"raw\":null") == -1:
#     emailList = re.findall(r'"normalized":".+,"badges"', rvInfoContent)
#     if emailList[0].find('@') != -1:
#         # print("https://www.amazon.com" + infoUrl)
#         global rowCount # 定义外部变量
#
#         # soup = bs(rvInfoContent, "html.parser")
#         #
#         # li_list = soup.find_all('span', attrs={'class': re.compile('a-size-extra-large')})
#         nameList = re.findall(r'"nameHeaderData":{"name":".+","profileExists"', rvInfoContent)
#         newWs.write(rowCount, 0, nameList[0][26:len(nameList[0]) - 17])
#         print(nameList[0][26:len(nameList[0]) - 17])
#
#         # ,"normalized":"http://hawkeyeeod@gmail.com"},"badges":{
#         # emailList = re.findall(r'"normalized":".+,"badges"', rvInfoContent)
#         newWs.write(rowCount, 1, emailList[0][21:len(emailList[0]) - 11])
#         print("                           " + emailList[0][21:len(emailList[0]) - 11])
#
#         # "facebook", "url": "http://Facebook.com/awakenednutrition"
#         if rvInfoContent.find("\"facebook\",\"url\":null") == -1:
#             facebookAddress = re.findall(r'"facebook","url":"https://www\.facebook\.com/\w+"', rvInfoContent)
#             # FBList = pattern.match(rvInfoContent)
#             # FBline = FBList[0][37:len(FBList[0])]
#             newWs.write(rowCount, 2, facebookAddress[0][18:len(facebookAddress[0]) - 1])
#             print("                                                       " + facebookAddress[0][18:len(facebookAddress[0]) - 1])
#
#         # {"type": "youtube", "url": "https://www.youtube.com/user/Tw3akst3r?\u0026amp;ab_channel=Tw3akst3r","iconUrl"
#         # if rvInfoContent.find("\"type\":\"youtube\",\"url\":null") == -1:
#         #     youtuAddress = re.findall(r'{"type": "youtube", "url": "https://www.youtube.com/.+","iconUrl"', rvInfoContent)
#         #     print("                                                                                    " + youtuAddress[0])
#
#
#         newWs.write(rowCount, 3, "https://www.amazon.com" + infoUrl);
#         print("                                                                                                                           https://www.amazon.com" + infoUrl)
#         newWb.save('reviewerInfo.xls');
#         rowCount = rowCount + 1
#         return
#     # else :
#     #     return
#     return
#
# def openInfo(reviewerUrlList):
#     # Analysis reviewerInfo
#     for infoUrl in reviewerUrlList:
#         threading.Thread(target=searchEmail, args=(infoUrl,)).start()

            # table.write(rowCount, 0, "https://www.amazon.com" + infoUrl)
            # rowCount = rowCount + 1

def findSymbol(content):
    global rowCount  # 定义外部变量
    soup = bs(content, "html.parser")
    tbody_list = soup.find('tbody')
    tr_list = tbody_list.find_all('tr')
    # print(str(len(tr_list)))

    for tr_item in tr_list:
        time.sleep(10 + random.randint(0,10))
        detailContent = init_url("https://www.feixiaohao.com/currencies/" + tr_item['id'] + "/")
        if detailContent == "" :
            return
        detail_soup = bs(detailContent, "html.parser")
        fli_list = detail_soup.find('body').find_all('div', attrs={'class': re.compile('firstPart')})[0].find_all('div', attrs={'class': re.compile('cell')})[2].find_all('div', attrs={'class': re.compile('value')})
        sli_list = detail_soup.find('body').find_all('div', attrs={'class': re.compile('secondPark')})[0].find('ul').find_all('li')
        newWs.write(rowCount, 0, rowCount)
        # print(sli_list[0].find('span', attrs={'class': re.compile('value')}).contents[0]) #英文名字
        newWs.write(rowCount, 1, sli_list[0].find('span', attrs={'class': re.compile('value')}).contents[0])
        # print(sli_list[4].find('span', attrs={'class': re.compile('value')}).find('a')['href'])  #白皮书地址
        if (sli_list[4].find('span', attrs={'class': re.compile('value')}).find('a') != None) :
            newWs.write(rowCount, 2, sli_list[4].find('span', attrs={'class': re.compile('value')}).find('a')['href'])
        else :
            newWs.write(rowCount, 2, "-")


        # print(fli_list[0].contents[0])  #流通量
        newWs.write(rowCount, 3, fli_list[0].contents[0])
        # print(fli_list[1].contents[0])  #总发行量
        newWs.write(rowCount, 4, fli_list[1].contents[0])


        testdata = detail_soup.find('div',attrs={'class': re.compile('ct-chart ct-minor-second ct-chart2')}).find('div').find('span').contents[0]
        # print(testdata) #流通率
        newWs.write(rowCount, 5, testdata)


        introduction_url = detail_soup.find('div',attrs={'class': re.compile('des')}).find('a')['href']
        introductionContent = init_url("https://www.feixiaohao.com" + introduction_url)
        if introductionContent == "" :
            return
        introductionSoup = bs(introductionContent, "html.parser")
        introduction1 = introductionSoup.find('div',attrs={'class': re.compile('artBox')}).find_all('p')[0].contents[0]
        # introduction2 = introductionSoup.find('div',attrs={'class': re.compile('artBox')}).find_all('p')[1].contents[0]#.find('br').contents[0]
        print(introduction1)   #简介
        newWs.write(rowCount, 6, str(introduction1))

        newWb.save('SymbolData.xls');
        rowCount = rowCount + 1

    # for tr_item in tr_list :
    #     detailContent = init_url("https://www.feixiaohao.com/currencies/" + tr_item['id'] + "/")
    #
    #     print(tr_item['id'])


oldWb = xlrd.open_workbook('SymbolData.xls');
newWb = copy(oldWb);
newWs = newWb.get_sheet(0);

firstContent = init_url("https://www.feixiaohao.com")
if firstContent != "" :
    findSymbol(firstContent)

for i in range(2, 6):
    time.sleep(10 + random.randint(0,9))
    nextPageContent = init_url("https://www.feixiaohao.com/list_" + i + ".html")
    if nextPageContent != "":
        findSymbol(nextPageContent)


# for i in range(2, 5):
#     # get reviewer url
#     time.sleep(3 + random.randint(2, 4))
#     rvListContent = init_url("https://www.feixiaohao.com" + str(i) + "?page=" + str(i));
#     reviewerUrlList = re.findall(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', rvListContent)
#     # print(reviewerUrlList)
#     print("第 " + str(i) + " 页")
#
#     threading.Thread(target=openInfo, args=(reviewerUrlList,)).start()
