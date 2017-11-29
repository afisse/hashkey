import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python.org/')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
