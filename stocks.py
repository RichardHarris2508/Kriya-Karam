import re
import urllib.request

#https://www.google.com/search?q=

url = "https://www.google.com/search?q=NASDAQ:+"
stock = input("Enter your stock   ")
url = url + stock

req = Request(url, headers={'User-Agent': 'Google'})

data = urllib.request.urlopen(req).read()
data1 = data.decode('latin-1')

m = re.search('meta itemprop="price"',data1)

start = m.start()
end = start + 50

newString = data1[start:end]

m = re.search('content=""', newString)
start = m.end()

newString1 = newString[start:]

m = re.search("/", newString1)
start = 0
end = m.end()-3

final = newString1[0:end]

print(final)

