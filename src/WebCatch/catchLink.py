import requests
import re
import os

url = "http://www.postgres.cn/docs/11/runtime-config-resource.html"
urlBox = []
def catchURL(url):
    file = requests.get(url,timeout=5)
    data = file.content
    links = re.findall(r'(https?://[^\s)";]+\.(\w|/)*)',str(data))
    for i in links:
        try:
            currentURL = i[0]
            if currentURL not in urlBox:
                urlBox.append(currentURL)
                sql = """
ssh pgadmin@10.211.55.8 psql test -U pgadmin <<EOF
insert into url values(nextval(\'url_seq\'), \'"""+currentURL+"""\');
EOF
"""
                print(sql)
                os.popen(sql)
                print(currentURL)
                catchURL(currentURL)
        except Exception as e:
            pass
            continue




catchURL(url)