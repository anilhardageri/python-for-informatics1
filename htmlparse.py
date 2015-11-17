import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
x = 0
y = 0
total = 0
for tag in tags:
   # Look at the parts of a tag
   x = tag.contents[0]
   y = int(x)   
   total = total + y
 
print total
 