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
    req.add_header("Cookie", "lc-main=en_US; x-wl-uid=1Wxr9a8HKeo9AbKEncf0d5UKEmW/rKuXoB9uQl/9GDt6CWJCj+OZNBeK5mpqnW4USK1sPaVO7OggZat2LshsbTVBT5YZRiRa2a6EoeHefDj7ZTzpYTjcORvvVvTwvRrwh+LkyBxUsqDk=; s_vnum=1947139795319%26vn%3D1; s_nr=1515139817164-New; s_dslv=1515139817166; x-main=o0xoT065JxdUujnf9TXG0gpyziZgeQkzoRYUODrXpTvX23hPfCACKAsMvUxeOlSD; at-main=Atza|IwEBIG5hGWG3vLUnDW6bCOMA4WgKRJHYM_az64kMNL8IucHjubzqqSfg9fTLQvsYZPtP9sCuI1JR5EmyUtcr5vEq0usmWUpHayYQjOXlTRwbPNnulN05tk-In6PYv27ksrBV1pVc2faj2c8NJI4PSJaSF_Iq7L0f7Si0bTM8h1wCi7YD4lLdZX895l1LgKbTGo6K0m11ZRkjOyJc9EN-piKE6gURRFNNFMQJkivsZJxOSK0Kfm-0ZWLnK97Oj3Nof-TaJFaUmVupI7Q0ixSRcU71nv_Fc5N7B1lzlmD9msl2IepNWF0NS7TEMCh3SQeXnx5KNdIxszEnGZQv-grIf0J83ahD_M5PCeyaYPmJnnn8CPpqCrc2BH47aC_hXAagduMMJPnkgLxqo_UL0xkzdgxyrFCR; sst-main=Sst1|PQHUHSLljqi8C_CP5coNs318CHHIVumHu_1Tw8pSlOmplr6IjhpeRNnjFstRSo4tgvEM288tHNK52Lth3KFgJbrSWXvjAvIR97dpaxC54gzXycXpVAY93yWVtFoy8GIRF4YCalazjN6gc-2028OQLhtZl6KZ2uB7DKhDjzr1kEGt4O-DOFD1T4RtGAfR2Y8qArwg1Ju-9qrOUdz7L-3ZuUC4aT2QvFTiLsUmPPbkhCD6WM8dhs9izp4aeBtwHj_GxmxC6j14vUKR8AR3VKMuaB79KA; spblockdate=1515403611991; ubid-main=132-9310496-5343729; session-id-time=2082787201l; session-id=140-1431192-8975455; skin=noskin; session-token=\"Duw2ZoqJeMr8BME5ADQzNm2fJxBuGwQr9AmNtzRMRJ7qRoq9wL7kDBj+IaFNXnl0P+HvE4aWij3/a1KJlG+vqZTUfQs626QnJClzHZwza3LlvSiokBQ4HIlZhkksewlZxGWYGo6estHwY/yuvrZhNyVMSwEJpPU7ZmB93g1hv1FAHTgIG5DM5oXfX/SV/bkeyKo5cSq9WPOmtuGDwSTirEBJKBj2RsVCnK7gZeNZB2n9ZmqutmAk7M6oDrB/VWK7B9aSzorVHJNtzOGF7fL5Bg==\"; csm-hit=tb:7E52FW8S3R5BARNKGYHA+s-QZWPN1GRH4HD4HGBVSSA|1524580119977&adb:adblk_no")


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
    soup = bs(rvInfoContent, "html.parser")

    a_list = soup.find_all('a', attrs={'class': re.compile('social-link-image')})
    if len(a_list) > 0:
        for link in a_list:
            print(link)

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


for i in range(24, 1000):
    # # get reviewer url
    # time.sleep(3 + random.randint(2, 4))
    # rvListContent = init_url("https://www.amazon.com/hz/leaderboard/top-reviewers/ref=cm_cr_tr_link_" + str(i) + "?page=" + str(i));
    # reviewerUrlList = re.findall(r'/gp/profile/amzn1.account.\w+/ref=cm_cr_tr_tbl_.{1,7}_name', rvListContent)
    # # print(reviewerUrlList)
    # print("第 " + str(i) + " 页")
    #
    # threading.Thread(target=openInfo, args=(reviewerUrlList,)).start()
    rvInfoContent = init_url("https://www.amazon.com/gp/profile/amzn1.account.AHQCAHFHCSWSUAXSWRSV44S233MA/ref=cm_cr_tr_tbl_235_name")
    soup = bs(rvInfoContent, "html.parser")
    a_list = soup.find_all('a', attrs={"rel": "noopener noreferrer"})
    if len(a_list) > 0:
        for link in a_list:
            print(link)