import http.cookiejar
from urllib import request

cookie = http.cookiejar.LWPCookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(opener)
# response3 = request.urlopen("https://www.amazon.com")
req = request.Request("https://www.amazon.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
req.add_header("Host", "www.amazon.com")
req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
req.add_header("Host", "www.amazon.com")
req.add_header("Upgrade-Insecure-Requests", "1")
req.add_header("Connection", "keep-alive")
req.add_header("Cache-Control", "max-age=0")

resp = request.urlopen(req)
htmlContentBuf = resp.read().decode('utf-8')
print(htmlContentBuf)
resp.close()