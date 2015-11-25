import urllib
from BeautifulSoup import *
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
uh = urllib.urlopen(url)
data = uh.read()
commentinfo = ET.fromstring(data)
lst = commentinfo.findall('comments/comment')
print 'user count:', len(lst)
total = 0
for item in lst:
     
    ext = item.find('count').text
    ext1 = int(ext)
    total = total + ext1
    
       
print total













