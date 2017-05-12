from urllib import urlopen
from xml.etree.ElementTree import parse

url="http://planet.python.org/rss20.xml"
doc=parse(urlopen(url))

for i in doc.iterfind('channel/item'):
   title = i.findtext('title')
   print(title)
  
