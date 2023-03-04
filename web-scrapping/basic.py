from bs4 import BeautifulSoup
import requests

req = requests.get('https://es.wikipedia.org/wiki/Cliente-servidor')
# print(req.content) #html content

# to see in a better way
soup = BeautifulSoup(req.content)
print(soup.prettify)
