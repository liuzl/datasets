import requests
import re
import pyce3
import json

#url = 'http://kw.beijing.gov.cn/col/col114/index.html?pageNum=1&uid=1737'

def get_links(url):
    ret = requests.get(url)
    page = ret.content.decode('utf-8', 'ignore')
    links = re.findall(r'<h3 style="min-height:55px"><span></span><a href="(.+?)"', page)
    links = ['http://kw.beijing.gov.cn'+link for link in links]
    return links

url = "http://kw.beijing.gov.cn/module/web/jpage/dataproxy.jsp?page=1&appid=1&appid=1&webid=1&path=/&columnid=114&unitid=1737"
links = get_links(url)
out = open("file.json", "w")
for link in links:
    print("link: ", link)
    html = requests.get(link).content
    _, time, title, text, _ = pyce3.parse(link, html)
    item = {"url":link, "time":time, "title":title, "text": text}
    out.write(json.dumps(item, ensure_ascii=False)+"\n")
out.close()
