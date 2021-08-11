# 使用Xpath解析html网页内容

from lxml import etree

if __name__ == '__main__':
    f = open('shy.html', 'r', encoding='utf-8')
    con = f.read()
    f.close()

    html = etree.HTML(con)

    # 解析所以的节点
    # result = html.xpath("//*")
    # result = html.xpath("a")
    result = html.xpath("/")
    for i in result:
        print(i.tag, end=" ")
        a = i.find('a')
        print(a.get("href"))


    # result = html.xpath("//")

