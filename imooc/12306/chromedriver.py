from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
import time


path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

url = "https://www.huomao.com/channel/lol"

# 司机开车了
driver.get(url)

# 让页面移到最下面点击加载，连续6次，司机会自动更新！！
for i in range(6):
    driver.find_element_by_id("getmore").click()
    time.sleep(1)

# 开始解析
soup = BeautifulSoup(driver.page_source, "html.parser")
page_all = soup.find("p", attrs={"id": "channellist"})
pages = page_all.find_all("p", attrs={"class": "list-smallbox"})

name = []
title = []
watching = []

for page in pages:
    tag = False
    try:
        this_title = page.find("p", attrs={"class": "title-box"}).find("em").string.strip()
        temp = page.find_all("p")
        this_name = temp[1].find("span").string.strip()
        this_watching = temp[1].find_all("span")[1].string.strip()
        tag = True
        if tag:
            title.append(this_title)
            name.append(this_name)
            watching.append(this_watching)
    except:
        continue
result = DataFrame({
    "主播名": name,
    "节目名": title,
    "在线观看人数": watching
})

# 没有文件会自动创建
result.to_excel("E:\\resultLol.xlsx", sheet_name="Sheet1")