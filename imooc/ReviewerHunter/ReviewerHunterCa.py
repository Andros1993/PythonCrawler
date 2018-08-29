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


def init_url(url, urlbuf, pageUrl):
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
    req.add_header("authority", "www.amazon.ca")
    req.add_header("method", "GET")
    if (urlbuf != "") :
        req.add_header("path", urlbuf)
    req.add_header("scheme", "https")
    req.add_header("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    req.add_header("accept-encoding", "deflate, br")
    req.add_header("accept-language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
    req.add_header("cache-control", "max-age=0")
    req.add_header("refererl", pageUrl)
    req.add_header("upgrade-insecure-requests", 1)
    req.add_header("Cookie", "session-id=130-3385262-3181101; session-id-time=2082787201l; ubid-acbca=131-0931675-1916457; x-acbca=IcR6yFsAntlxu4QraZewMLr7x6mo6D1o5xrf8ab2pdddliH7oJal5joqHIG9kE42; at-acbca=Atza|IwEBIEnZdWYQe4nLl2snBss6l4YAyadKYpK3glYky1sYlHnxeorEenSrTmqWAlw2xguHIE_oOUBHKqAICMcIzCjlYMW81LBDiaWzZS037XB9O_KEAAjWYNseBV11UUJ0RaMl58W5b5Won_z-fQrUCvYjvH3415Pk7JTFpVPYoW37jdVZYt8Utya_3d3dNPFedKe8nb964TWrYXW4MpI6aNASjYDeQEtN-WnJ4hRLI-xgOrUM7eCA_CMwSMD23ziXipa8Eggo_C3kd8YxY3qGDtZn9QSOxhrka0PWiwpbD65PJIifctyuxQN26ragb07GzuGonqrY7n2T_armSr5BgXZ1PmOjd0bsadS6w0Hrq9qa3AnROiPM43wC-ZRI7aF1lW098G04aGWrPptrS0pztmxTaTWdim6d0bBItnWNd82xvyd-lovXfQGGC9t9Oi7mBDnVOr8; sess-at-acbca=\"N7T5dHJZKWt7mwftQVlP1kaWSePOVLenga3aDvBq7uw=\"; sst-acbca=Sst1|PQF6ri4Y9LPxWZ8_v6nQpiFkC4exUE0lG6vVqKZZdETMDozzyUjyIWe9dYgvvNz2UKnjLNYpIK9dUpRIKnWRFN8Z9nzLfDlkeXtnZOffKT6K8V-s4vPbtK7LR4fO8Ebfm3hFT4OQFJ_kYphS05YWgnJ6-cVy_9RAufGuiRa3uSqYa1Gv0aj2iolV49wPwfSKx3cGm2saBXrZQnbsmF5gk0a5sBcctkUs62i5k1OhROV_rSh0qgXsNB0dLD1fAPElOP5mQkONjD65kmZpHnokEJy9ASyg2H6YOPcKuod_3Ryqmi7CrduhT1xiOj0LkS0-3UUPRhtWcXN-JGkUdNjqR9g2Wg; lc-acbca=en_CA; x-wl-uid=1mno3xQ2PgntCz2x/G7RO2tol8qqazuqr3xeocpQu9/mbZoDR20QD8x7rRX0jaBV2r5Z7r1xpnK0sF4uSoWnPEKPHTTx4FtYzSOKZFyl92tndMq+KPS98189FJ5WIzKmnumXBLnKhyYo=; session-token=\"86UaTNsl4Ei63S21hnyNB6WMUS6rIPDfiJDgvTOeuSI/jNXgSS6YnuWe0jhDLy7XjVFv7SVEhb2fBpzxNmRQLZzWy6odj1Zid4ZLW0eukPJXrc4bFUfFIhK+B69TROtjfGSZnmzCqNsOc05o95NTQP++an8lrnN3TUmRJ+wRH3k7FUbh8l3Opv+HWgQzMUp0rJb1keCpy2m96XqKuw9Y4lL6KNYdEvIXDXnmEb7S6/yPSyNcTHegD/QUXKD4fEy/q/9/ViakqNo/dByhGQLROw==\"; csm-hit=tb:JEE5WNZ4W5XWH6XHQWX2+b-K7E31R0P9ZK3K8GFDB4J|1535505056285&adb:adblk_yes")


    resp = request.urlopen(req)
    htmlContentBuf = resp.read().decode('utf-8')
    return htmlContentBuf;

# # 新建一个excel文件
# file = xlwt.Workbook()
# # 新建一个sheet
# table = file.add_sheet('info', cell_overwrite_ok=True)
#
rowCount = 0;

def searchEmail(infoUrl, pageUrl):
    rvInfoContent = init_url("https://www.amazon.ca" + infoUrl, infoUrl, pageUrl)
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
        print("                 " + emailList[0][21:len(emailList[0]) - 11])
        print("                                                                       https://www.amazon.com" + infoUrl)

        # {"type": "youtube", "url": "https://www.youtube.com/user/Tw3akst3r?\u0026amp;ab_channel=Tw3akst3r","iconUrl"
        # if rvInfoContent.find("\"type\":\"youtube\",\"url\":null") == -1:
        #     youtuAddress = re.findall(r'{"type": "youtube", "url": "https://www.youtube.com/.+","iconUrl"', rvInfoContent)
        #     print("                                                                                    " + youtuAddress[0])


        newWs.write(rowCount, 3, "https://www.amazon.ca" + infoUrl);
        newWb.save('reviewerInfoCa.xls');
        rowCount = rowCount + 1
        return
    # "facebook", "url": "http://Facebook.com/awakenednutrition"
    if rvInfoContent.find("\"facebook\",\"url\":null") == -1:
        facebookAddress = re.findall(r'"facebook","url":"https://www\.facebook\.com/\w+"', rvInfoContent)
        # FBList = pattern.match(rvInfoContent)
        # FBline = FBList[0][37:len(FBList[0])]
        if (len(facebookAddress) > 0):
            newWs.write(rowCount, 2, facebookAddress[0][18:len(facebookAddress[0]) - 1])
            print("                   " + facebookAddress[0][18:len(facebookAddress[0]) - 1])
            print("                                                                       https://www.amazon.com" + infoUrl)
            rowCount = rowCount + 1
    return

def openInfo(reviewerUrlList, pageUrl):
    # Analysis reviewerInfo
    for infoUrl in reviewerUrlList:
        time.sleep(3 + random.randint(4, 9))
        threading.Thread(target=searchEmail, args=(infoUrl,pageUrl,)).start()

            # table.write(rowCount, 0, "https://www.amazon.com" + infoUrl)
            # rowCount = rowCount + 1


oldWb = xlrd.open_workbook('reviewerInfoCa.xls');
newWb = copy(oldWb);
newWs = newWb.get_sheet(0);


for i in range(756, 1000):
    # get reviewer url
    time.sleep(3 + random.randint(7, 10))
    pageUrl = "https://www.amazon.ca/hz/leaderboard/top-reviewers/ref=cm_cr_tr_link_" + str(i) + "?page=" + str(i)
    rvListContent = init_url(pageUrl, "", pageUrl);
    reviewerUrlList = re.findall(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', rvListContent)
    # print(reviewerUrlList)
    print("第 " + str(i) + " 页")

    threading.Thread(target=openInfo, args=(reviewerUrlList,pageUrl,)).start()
