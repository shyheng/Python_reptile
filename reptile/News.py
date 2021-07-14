# 爬取百度新闻的链接信息
from urllib import request
import re

url = "https://news.baidu.com/"

req = request.Request(url)

res = request.urlopen(url)

html = res.read().decode('utf-8')

pat = '<a href="(.*?)" target="_blank" mon=".*?">(.*?)</a>'

dlist = re.findall(pat,html)

for a in dlist:
    print(a[1]+":"+a[0])





