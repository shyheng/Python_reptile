from urllib import request
import re

if __name__ == '__main__':
    url = "http://www.mi.com/buy/detail?product_id=10000214"

    req = request.Request(url)
    res = request.urlopen(req)

    print(res.status)
    html = res.read().decode('utf-8')

    pat = '<title>(.*?)</title>'
    str = re.findall(pat, html)
    print(str)