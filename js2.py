import json
import urllib

url = raw_input('Enter URL: ')
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(data)
total = 0
for u in js['comments'] :
  q = u['count']
  w = int(q)
  total = total + w

print total
  
    
