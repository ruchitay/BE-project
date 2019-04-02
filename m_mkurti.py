import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
  

try: 
    conn = MongoClient('mongodb://localhost:27017' ) 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.rtpa


url = 'https://www.myntra.com/amp/men-ethnic-wear?rows=500&p=1'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'html.parser')
pqr  = soup.findAll("div",{"class" : "product"})
#pqr  = soup.findAll("a",{"class" : "_2mylT6"})
y = len(pqr)

while y != 0 :
	for ac in pqr :
		product_link = str(ac.a["href"])
		myntra_homepage = "https://www.myntra.com/amp"
		product_link1 = myntra_homepage + product_link
		myntra_homepage1 = "https://www.myntra.com"
		product_link2 = myntra_homepage1 + product_link
		print(product_link2)
		image = ac.find("amp-img")
		image= image.get('src')
		print(image)
		price = ac.findAll("span",{"class" : "price-discounted"})
		price = price[0].text
		print("price:" + price)
		source_code = requests.get(product_link1)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,'html.parser')
		xyz  = soup.findAll("div",{"class" : "pdp-price-info"})
		for link in xyz :
			name = link.find("h1",{"class":"pdp-title"}).text
			print("name:"+ name)
		db.myindex1.insert_one(
    	{
    	'title': name,
        'price' : price,
        'product_links': product_link2,
        'images' : image
    	})
    
   


    