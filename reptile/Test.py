from urllib import request

url = 'https://www.baidu.com'

res = request.urlopen(url)

print(res.status)
print(res.version)
print(res.reason)
print(res.geturl())

print(res.read().decode('utf-8'))

