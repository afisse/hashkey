import urllib2, json
from bs4 import BeautifulSoup


f = urllib2.urlopen('http://www.licitor.com/ventes-aux-encheres-immobilieres/provence-alpes-cote-d-azur.html')
html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

page_total = soup.find(class_="PageTotal")
print page_total

ul = soup.find(class_="AdResults")
lis = ul.find_all('li')

ads=[]

for li in lis:
    ad={}

    href = li.a["href"]
    ad["href"] = href

    title = li.a["title"]
    ad["title"] = title

    number = li.a.find(class_="Location").find(class_="Number").string
    city = li.a.find(class_="Location").find(class_="City").string
    ad["location"] = {"number":number,"city":city}

    name = li.a.find(class_="Description").find(class_="Name").string
    text = li.a.find(class_="Description").find(class_="Text").string
    ad["description"] = {"name":name,"text":text}

    initial_price = li.a.find(class_="Footer").find(class_="Price").find(class_="Initial").find(class_="PriceNumber").string
    ad["initial_price"] = initial_price

    span = li.find(class_="PublishingDate").span
    if span is None:
        ad["publishing_date"] = ""
    else:
        ad["publishing_date"] = span.string
    ads.append (ad)

print (json.dumps(ads,indent=2))
