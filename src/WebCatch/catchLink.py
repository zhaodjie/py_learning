import requests
import re

url = "https://www.autohome.com.cn/shanghai/"
urlBox = []
def catchURL(url):
    file = requests.get(url,timeout=2)
    data = file.content
    links = re.findall(r'(https?://[^\s)";]+\.(\w|/)*)',str(data))
    print(links)
    for i in links:
        try:
            currentURL = i
            urlBox.append(currentURL)
            #print(currentURL)
            catchURL(currentURL)
        except Exception as e:
            pass
        continue



catchURL(url)