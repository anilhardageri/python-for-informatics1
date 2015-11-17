import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))-1
urllist = list()
urllist.append(url)

print 'Retrieving: ', urllist[0]


for i in range(count):
    html = urllib.urlopen(urllist[-1]).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    taglist = list()
    for tag in tags:
       taglist.append(tag)
    url = taglist[pos].get('href', None)
    print 'Retrieving: ', url
    urllist.append(url)
print 'Last Url: ', urllist[-1]