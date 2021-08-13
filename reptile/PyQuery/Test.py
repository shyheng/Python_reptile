# 使用pyQuery解析html

from pyquery import PyQuery as pq

if __name__ == '__main__':
    doc = pq(filename='shy.html',encoding="utf-8")

    # print(doc("title"))
    # print(doc("#shy1"))
    # print(doc("a[href*='b']"))
    alist = doc("ul li a")
    print(type(alist))
    print(type(alist.items()))
    for i in alist.items():
        print(i.attr.href)

