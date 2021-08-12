from bs4 import BeautifulSoup

if __name__ == '__main__':
    f = open("shy.html", 'r', encoding='utf-8')
    con = f.read()

    f.close()

    soup = BeautifulSoup(con, 'lxml')

    # 第一种节点解析器
    # print(soup.title)
    # 获取ul并从ul中获取所有子节点
    blist = soup.ul.children

    # 遍历
    for li in blist:
        # print(li)
        if li.name == 'li':
            a = li.a
            print(a.string,':',a.attrs['href'])