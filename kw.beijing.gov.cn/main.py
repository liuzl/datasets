import requests
import re
url = 'http://kw.beijing.gov.cn/col/col114/index.html?pageNum=1&uid=1737'

def get_links(url):
    ret = requests.get(url)
    page = ret.content.decode('utf-8', 'ignore')
    links = re.findall(r'<h3 style="min-height:55px"><span></span><a href="(.+?)"', page)
    links = ['http://kw.beijing.gov.cn'+link for link in links]
    print(len(links))
    return links
'''
urls = set()
for i in range(1, 7):
    url = 'http://kw.beijing.gov.cn/col/col114/index.html?pageNum=%d&uid=1737' % i
    links = get_links(url)
    urls.update(links)
    print(i, len(urls))
'''

url = "http://kw.beijing.gov.cn/module/web/jpage/dataproxy.jsp?page=1&appid=1&appid=1&webid=1&path=/&columnid=114&unitid=1737"
links = get_links(url)
for link in links:
    print(link)
print(len(set(links)))
