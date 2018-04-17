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
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    req.add_header("Host", "www.amazon.com")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("Host", "www.amazon.com")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("Cookie", "x-main=Rce3DZGa7QL8Xf2cUrEd5VrO1jVvYrkI97c91jIzIQ7mv66O8L8U8EaExQKA96Cs; "
                             "at-main=Atza|IwEBIIEzwtjMJsqjVca9O1rYZ2w0JFuce96rnQ9NQ0VLnkbUQiTJ5wO5_Kd5_fi5Ex8z"
                             "8cNbpsv45AP4c5NBs8bgIJbjHftEh2_0F7QtY4M30PGxnvJj5skIB7dF9RXzn8cXS1M_Mligzhrnw6pCjC"
                             "Uu1We16AiTZMIeOWVCvga6GuhZud5Pt0VBa84HNTteaqH8ieiW0vFS_tjJGOuy5SBe5WbXH7hA0ojdfvOyzt"
                             "4hmj_Aw0qHqyz_CD7HtlRIwzv1j-uXq4pvppY4tQunROpg41Um26w0g2cmnKCBwSL01IQSXa2jSmQ4DMJ0zU9Wg2"
                             "HeZYv3WA21772TahWwHU9cvM93mGePZpqkfznR5sWS_80MQkQJ4A4xgj5hq9Tz2zDKrOpOZoeU9lf0-WgNTrHYJTg0; "
                             "lc-main=en_US; x-wl-uid=1Wxr9a8HKeo9AbKEncf0d5UKEmW/rKuXoB9uQl/9GDt6CWJCj+OZNBeK5mpqnW4USK1s"
                             "PaVO7OggZat2LshsbTVBT5YZRiRa2a6EoeHefDj7ZTzpYTjcORvvVvTwvRrwh+LkyBxUsqDk=; skin=noskin; session-token"
                             "=\"f+uPDH/1jpYoaFhxC6LIrJoH+9Ua1EDfXbT0uf0WPePXJyRau3I0/p/KgpfEbGU+e5QKp3ucx9A6LMuFZBpa9Av77+bGpF/dTk"
                             "SmIP5JxWABrCWNcl4oTT1qHdbF9jzL5hosYkY42pRqKnxgYvAuiACx/V0QKPPuT3WfM8KuckfDlxqS6+BwuSwsnmPQi2i677BVgGuDu"
                             "IAFWR2sc5e7K2VB7R1zftr1UlxDCWKtnLfRjx51BKlyorv3ZTjhqrc/69ZmwTE29Os5aIsm/qB32g==\"; ubid-main=132-9310496-"
                             "5343729; session-id-time=2082787201l; session-id=140-1431192-8975455; csm-hit=D5YYND20TR0GYJ9TGD1M+b-H8BWB7GQ57YG1YSXJHJV|1512219757447")


    resp = request.urlopen(req)
    htmlContentBuf = resp.read().decode('utf-8')
    return htmlContentBuf;

# # 新建一个excel文件
# file = xlwt.Workbook()
# # 新建一个sheet
# table = file.add_sheet('info', cell_overwrite_ok=True)
#
rowCount = 0;

def searchEmail(infoUrl):
    rvInfoContent = init_url("https://www.amazon.com" + infoUrl)
    if rvInfoContent.find("\"raw\":null") == -1:
        emailList = re.findall(r'"normalized":".+,"badges"', rvInfoContent)
        if emailList[0].find('@') != -1:
            # print("https://www.amazon.com" + infoUrl)
            global rowCount # 定义外部变量

            # soup = bs(rvInfoContent, "html.parser")
            #
            # li_list = soup.find_all('span', attrs={'class': re.compile('a-size-extra-large')})
            nameList = re.findall(r'"nameHeaderData":{"name":".+","profileExists"', rvInfoContent)
            newWs.write(rowCount, 0, nameList[0][26:len(nameList[0]) - 17])
            print(nameList[0][26:len(nameList[0]) - 17])

            # ,"normalized":"http://hawkeyeeod@gmail.com"},"badges":{
            # emailList = re.findall(r'"normalized":".+,"badges"', rvInfoContent)
            newWs.write(rowCount, 1, emailList[0][21:len(emailList[0]) - 11])
            print("                           " + emailList[0][21:len(emailList[0]) - 11])

            # "facebook", "url": "http://Facebook.com/awakenednutrition"
            if rvInfoContent.find("\"facebook\",\"url\":null") == -1:
                facebookAddress = re.findall(r'"facebook","url":"https://www\.facebook\.com/\w+"', rvInfoContent)
                # FBList = pattern.match(rvInfoContent)
                # FBline = FBList[0][37:len(FBList[0])]
                # newWs.write(rowCount, 2, FBline)
                print("                                                       " + facebookAddress[0])

            # {"type": "youtube", "url": "https://www.youtube.com/user/Tw3akst3r?\u0026amp;ab_channel=Tw3akst3r","iconUrl"
            if rvInfoContent.find("\"type\":\"youtube\",\"url\":null") == -1:
                youtuAddress = re.findall(r'{"type": "youtube", "url": "https://www.youtube.com/.+","iconUrl"', rvInfoContent)
                print("                                                                                    " + youtuAddress[0])


            newWs.write(rowCount, 3, "https://www.amazon.com" + infoUrl);
            print("                                                                                                                           https://www.amazon.com" + infoUrl)
            newWb.save('reviewerInfo.xls');
            rowCount = rowCount + 1
            return
    else :
        return
    return

def openInfo(reviewerUrlList):
    # Analysis reviewerInfo
    for infoUrl in reviewerUrlList:
        threading.Thread(target=searchEmail, args=(infoUrl,)).start()

            # table.write(rowCount, 0, "https://www.amazon.com" + infoUrl)
            # rowCount = rowCount + 1


oldWb = xlrd.open_workbook('reviewerInfo.xls');
newWb = copy(oldWb);
newWs = newWb.get_sheet(0);


for i in range(85, 100):
    # get reviewer url
    time.sleep(5 + random.randint(2, 4))
    rvListContent = init_url("https://www.amazon.com/hz/leaderboard/top-reviewers/ref=cm_cr_tr_link_" + str(i) + "?page=" + str(i));
    reviewerUrlList = re.findall(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', rvListContent)
    # print(reviewerUrlList)
    print("第 " + str(i) + " 页")

    threading.Thread(target=openInfo, args=(reviewerUrlList,)).start()
