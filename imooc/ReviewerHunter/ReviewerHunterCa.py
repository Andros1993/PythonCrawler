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
    req.add_header("Host", "www.amazon.ca")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("Host", "www.amazon.ca")
    req.add_header("Upgrade-Insecure-Requests", "1")
    req.add_header("Connection", "keep-alive")
    req.add_header("Cache-Control", "max-age=0")
    req.add_header("Cookie", "session-id=130-3385262-3181101; "
                             "session-id-time=2082787201l; ubid-acbca=131-0931675-1916457; "
                             "a-ogbcbff=1; session-token=5PiOkEluZElZEVvmhvbDUKNqf2phmYyK9c2fo"
                             "IOki5XTM6fNBSFJJyC/lgbwZH5R4roQltzI/PsUtRGq1PdCUhi9Gc1gdQVVVWU47"
                             "7rcrdFNxqqlPrwjBADWygvfXC2uqioNcH8uXPTGmkiK4gdp273lHfYKFfhbRYvFt"
                             "p5o4n+noVatfIqSyZyFXQ4H6tOK3werFo6lQ+zsPE3+G4pK3M5zsCTztz+lRc3Nc"
                             "3V5JeAvtY94Z7mPWqYjZRPh/eGJknYmHIv/WCatECy7FP/yNydFSp1cW200; x-a"
                             "cbca=IcR6yFsAntlxu4QraZewMLr7x6mo6D1o5xrf8ab2pdddliH7oJal5joqHIG"
                             "9kE42; at-acbca=Atza|IwEBIEnZdWYQe4nLl2snBss6l4YAyadKYpK3glYky1s"
                             "YlHnxeorEenSrTmqWAlw2xguHIE_oOUBHKqAICMcIzCjlYMW81LBDiaWzZS037XB"
                             "9O_KEAAjWYNseBV11UUJ0RaMl58W5b5Won_z-fQrUCvYjvH3415Pk7JTFpVPYoW3"
                             "7jdVZYt8Utya_3d3dNPFedKe8nb964TWrYXW4MpI6aNASjYDeQEtN-WnJ4hRLI-x"
                             "gOrUM7eCA_CMwSMD23ziXipa8Eggo_C3kd8YxY3qGDtZn9QSOxhrka0PWiwpbD65"
                             "PJIifctyuxQN26ragb07GzuGonqrY7n2T_armSr5BgXZ1PmOjd0bsadS6w0Hrq9q"
                             "a3AnROiPM43wC-ZRI7aF1lW098G04aGWrPptrS0pztmxTaTWdim6d0bBItnWNd82"
                             "xvyd-lovXfQGGC9t9Oi7mBDnVOr8; sess-at-acbca=\"N7T5dHJZKWt7mwftQV"
                             "lP1kaWSePOVLenga3aDvBq7uw=\"; sst-acbca=Sst1|PQF6ri4Y9LPxWZ8_v6n"
                             "QpiFkC4exUE0lG6vVqKZZdETMDozzyUjyIWe9dYgvvNz2UKnjLNYpIK9dUpRIKnW"
                             "RFN8Z9nzLfDlkeXtnZOffKT6K8V-s4vPbtK7LR4fO8Ebfm3hFT4OQFJ_kYphS05Y"
                             "WgnJ6-cVy_9RAufGuiRa3uSqYa1Gv0aj2iolV49wPwfSKx3cGm2saBXrZQnbsmF5"
                             "gk0a5sBcctkUs62i5k1OhROV_rSh0qgXsNB0dLD1fAPElOP5mQkONjD65kmZpHno"
                             "kEJy9ASyg2H6YOPcKuod_3Ryqmi7CrduhT1xiOj0LkS0-3UUPRhtWcXN-JGkUdNj"
                             "qR9g2Wg; lc-acbca=en_CA; x-wl-uid=1alp8lkmwiwcbVFz1ZrPPw0IPhAIQH"
                             "imsfrkpgqYkZq6VCGHWZzClL0xNSrj5IpiRqZ2FpDlSZaxHKj4hJiwYirjk7ge5b"
                             "kd4un3cmgk3Rh0p6QqrlvkklZqiPfUfcAlS9S8pHDZn4sk=; csm-hit=tb:AN2P"
                             "6FSC3V3XMFV32H1N+s-F2MZ8QVWJMARZGR8Q2G7|1533302512294&adb:adblk_yes")


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
    rvInfoContent = init_url("https://www.amazon.ca" + infoUrl)
    # if rvInfoContent.find("\"raw\":null") == -1:
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
            newWs.write(rowCount, 2, facebookAddress[0][18:len(facebookAddress[0]) - 1])
            print("                                                       " + facebookAddress[0][18:len(facebookAddress[0]) - 1])

        # {"type": "youtube", "url": "https://www.youtube.com/user/Tw3akst3r?\u0026amp;ab_channel=Tw3akst3r","iconUrl"
        # if rvInfoContent.find("\"type\":\"youtube\",\"url\":null") == -1:
        #     youtuAddress = re.findall(r'{"type": "youtube", "url": "https://www.youtube.com/.+","iconUrl"', rvInfoContent)
        #     print("                                                                                    " + youtuAddress[0])


        newWs.write(rowCount, 3, "https://www.amazon.ca" + infoUrl);
        print("                                                                                                                           https://www.amazon.com" + infoUrl)
        newWb.save('reviewerInfoCa.xls');
        rowCount = rowCount + 1
        return
    # else :
    #     return
    return

def openInfo(reviewerUrlList):
    # Analysis reviewerInfo
    for infoUrl in reviewerUrlList:
        threading.Thread(target=searchEmail, args=(infoUrl,)).start()

            # table.write(rowCount, 0, "https://www.amazon.com" + infoUrl)
            # rowCount = rowCount + 1


oldWb = xlrd.open_workbook('reviewerInfoCa.xls');
newWb = copy(oldWb);
newWs = newWb.get_sheet(0);


for i in range(2, 1000):
    # get reviewer url
    time.sleep(3 + random.randint(2, 4))
    rvListContent = init_url("https://www.amazon.ca/hz/leaderboard/top-reviewers/ref=cm_cr_tr_link_" + str(i) + "?page=" + str(i));
    reviewerUrlList = re.findall(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', rvListContent)
    # print(reviewerUrlList)
    print("第 " + str(i) + " 页")

    threading.Thread(target=openInfo, args=(reviewerUrlList,)).start()
