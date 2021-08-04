# requests爬虫库的使用

import requests
import re

if __name__ == '__main__':
    url = "https://www.baidu.com"
    res = requests.get(url)
    print("status", res.status_code)
    # print(res.encoding)
    # res.encoding = "utf-8"
    # print(res.text)  # 获取响应内容

    html = res.content.decode("utf-8")
    # print(html)

    print(re.findall("<title>(.*?)</title>",html))
