import re
import urllib.request

url = 'http://time.is/just'
f = urllib.request.urlopen(url)

pattern = re.compile('<div id="twd">(.*?)</div>')
fText = f.read().decode('utf-8')
atomicTime = re.findall(pattern, fText)

print(atomicTime)