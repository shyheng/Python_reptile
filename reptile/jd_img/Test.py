# 图片信息爬取测试
# url地址：https://list.jd.com/list.html?9987,653,655

import requests
from pyquery import PyQuery as pq
from urllib.request import urlretrieve

if __name__ == '__main__':
    # 定义请求url地址
    url = "https://list.jd.com/list.html?9987,653,655"
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/30100101Firefox/4.0.1'
    }
    # 使用requests爬取指定url信息
    res = requests.get(url, headers=headers)
    conten = res.text

    # 使用PyQuery创建解析器
    doc = pq(conten)


    # 解析页面中的所有图片商品信息
    imlist = doc("img[width='220'][height='220']")


    # 遍历并解析图片url地址
    for im in imlist.items():
        imurl = "https:"+im.attr('src')
        m = 1
        urlretrieve(imurl,"./mypic/p"+str(m)+'.jpg')

        # # 存储图片
        # with requests.get(imurl,stream=True) as ir:
        #     with open("./mypic/p"+str(m)+'.jpg','wb') as f:
        #         for chunk in ir:
        #             f.write(chunk)

        m += 1










