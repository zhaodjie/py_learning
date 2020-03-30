import requests

url = "https://www.baidu.com"
res=requests.get(url)
print(res.content)
print(res.text)
