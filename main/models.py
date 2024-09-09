from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()           
    description = models.TextField()
    category = models.CharField(max_length=50)
    connection_type = models.CharField(max_length=50)
    layout = models.CharField(max_length=20)

    
    