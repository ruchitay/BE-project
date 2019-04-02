import time
from pymongo import MongoClient
from elasticsearch import Elasticsearch

mongodb_client = MongoClient('mongodb://localhost:27017')
es_client = Elasticsearch(['http://localhost:9200'])

mdb = mongodb_client['rtpa']

drop_index = es_client.indices.create(index='rtpa1', ignore=400)
create_index = es_client.indices.delete(index='rtpa1', ignore=[400, 404])

data = mdb.myindex1.find()

for x in data:
    _title = x['title']
    _price = x['price']
    _product_links = x['product_links']
    _images = x['images']

    #_category = x['category']
    #_description = x['description']
    #_link = x['link']

    doc = {

        'title': _title,
        'price' : _price,
        'project_links': _product_links,
        'images' : _images
        #'category': _category,
        #'description': _description,
        #'link': _link
    }

    res = es_client.index(index="rtpa1", doc_type="docs", body=doc)
    time.sleep(0.2)

print("Done")