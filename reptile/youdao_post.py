# 使用requests的post爬取数据
'''
爬取有道翻译的数据
'''

import requests
import re
import json



def youdao(keyword):
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        'i': keyword,
        'doctype': 'json'
    }

    # 发送请求
    res = requests.post(url,data=data)
    if res.status_code == 200:
        # 获取结果
        # json_data = json.loads(res.content.decode('utf-8'))
        json_data = res.json()
        print(json_data['translateResult'][0][0]["tgt"])
    else:
        print("请求失败")



if __name__ == '__main__':
    while True:
        keyword = input('请输入翻译的单词')
        if keyword == 'q':
            break
        youdao(keyword)