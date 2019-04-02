import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
  

try: 
    conn = MongoClient('mongodb://localhost:27017' ) 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.rtpa

def trade_spider(max_pages):
	page = 1

	while page <= max_pages:
		url = 'https://www.flipkart.com/amp/mens-clothing/ethnic-wear/pr?otracker=nmenu_sub_Men_0_Kurta%2C%20Pyjama%20%26%20more&sid=2oq%2Cs9b%2C3a0&start=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,'html.parser')
		xyz  = soup.findAll("div",{"class" : "_1HA1d"})
		#pqr  = soup.findAll("a",{"class" : "_2mylT6"})

		for link in xyz :
			product_links = link.findAll("a")
			product_links = product_links[0].get('href')
			print("link:" + product_links)
			price = link.findAll("p",{"class" : "_2lKKI"})
			price = price[0].text
			print("price:" + price)
			image = link.findAll("amp-img")
			image= image[0].get('src')
			print("image" + image)
			source_code = requests.get(product_links)
			plain_text = source_code.text
			soup = BeautifulSoup(plain_text,'html.parser')
			name = soup.find("h1", {"class": "_9E25nV"}).text
			print("name:"+ name)

			db.myindex1.insert_one(
				{
				'title': name,
        		'price' : price,
        		'product_links': product_links,
        		'images' : image
    			})

		page+=59							
trade_spider(1920)
