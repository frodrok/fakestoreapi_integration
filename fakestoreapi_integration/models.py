from django.db import models

from django.forms.models import model_to_dict

class Product(models.Model):
    title = models.CharField(max_length=255)
    
    price = models.FloatField()
    
    description = models.TextField()

    category = models.CharField(max_length=255)

    image = models.CharField(max_length=255)

    foreign_api_id = models.IntegerField()

    def to_dict(self):
        return model_to_dict(self)

class ProductRating(models.Model):
    
    rate = models.FloatField()
    count = models.IntegerField()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    def to_dict(self):
        return model_to_dict(self)

    
    

