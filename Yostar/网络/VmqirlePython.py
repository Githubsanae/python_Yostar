import os
import time

import requests
import re
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
}
res = requests.get('https://www.vmgirls.com/18229.html' ,headers=headers)
# print(res.request.headers)
# print(re.text)
html = res.text

dirName=re.findall('<span class="current">(.*?)</span>',html)[-1]
if not os.path.exists(dirName):
    os.mkdir(dirName)
# print(dirName)
urls=re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
for url in urls:
    time.sleep(0.5)
    fileName= url.split('/')[-1]
    resq=requests.get('http:'+url ,headers=headers)
    with open(dirName+'/'+fileName, "wb") as f:
        f.write(resq.content)
        print('提取中')
print('完成')
