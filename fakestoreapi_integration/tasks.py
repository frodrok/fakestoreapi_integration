import json
import urllib.request
import datetime

from django.utils import timezone
from django.db import models

from .models import Product, ProductRating

def fetch_store_api_data():

#    one_hour_ago = timezone.now() - timezone.timedelta(hours=1)

    ## Regular urllib user agent resulted in a 403 forbidden response
    parsed = None
    try: 
        url = "https://fakestoreapi.com/products"
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        
        
        response = urllib.request.urlopen(req)
        
        text = response.read()
        
        parsed = json.loads(text.decode('utf-8'))
        
    except:
        print("Couldn't fetch and parse the data")

    if not parsed:
        return
        
    for entry in parsed:
        print(entry)
        try:
            product = Product.objects.create(foreign_api_id=entry["id"],
                                             title=entry["title"],
                                             price=entry["price"],
                                             description=entry["description"],
                                             category=entry["category"],
                                             image=entry["image"])

            rating = ProductRating.objects.create(rate=entry["rating"]["rate"],
                                                  count=entry["rating"]["count"],
                                                  product=product)
            print(f"Successfully created database entry for ${entry}")
            
        except Exception as e:
            print(e)
            print(f"Couldn't create database entries for ${entry}")
                                             

        

#    print(json.loads(text.decode('utf-8')))
