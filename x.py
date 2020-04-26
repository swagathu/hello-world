import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ssl.verify_mode = ssl.CERT_NONE

x = urllib.request.urlopen(input('Enter url:')).read()
x1 = x.decode()
tree = ET.fromstring(x1)
list1 = list()
for i in tree.findall('comments/comment') :#findall returns a list of contents of comment under comments
    list1.append(int(i.find('count').text))#appending count tag data after converting data to int
print(sum(list1))
