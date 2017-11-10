import urllib,http.cookielib as cookielib
#创建cookie容器
cj = cookielib.CookieJar()
# 创建1个opener
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
#给urllib2安装opener
urllib.install_opener(opener)
#使用带有cookie的urllib2访问网页
response = urllib.urlopen("http://www.xxx.com")


#创建Request对象
request = urllib.Request(url)

#添加数据
request.add_data('a','1')

#添加http的header,伪装成浏览器登录
request.add_header('User-Agent','Mozilla/5.0')

#发送请求获取结果
response = urllib.urlopen(request)
