import requests
import re

if __name__ == '__main__':
    data = {
        'product_id': '10000214'
    }
    url = "http://www.mi.com/buy/detail"

    res = requests.get(url, params=data)

    print(res.status_code)

    html = res.content.decode('utf-8')

    pat = '<title>(.*?)</title>'
    str = re.findall(pat, html)
    print(str)