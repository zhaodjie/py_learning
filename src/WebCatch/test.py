import re
import urllib.request

def getlink(url):
	headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
	opener=urllib.request.build_opener()
	opener.addheaders=[headers]
	urllib.request.install_opener(opener)
	file=urllib.request.urlopen(url).read()
	data=str(file)
	pat='(https?://[^\s)";]+\.(\w|/)*)'
	link=re.compile(pat).findall(data)
	link=list(set(link))
	return link
url="http://blog.csdn.net/"
linklist=getlink(url)
for link in linklist:
	print(link[0])