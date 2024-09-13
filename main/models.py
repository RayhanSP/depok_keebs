from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()           
    description = models.TextField()
    category = models.CharField(max_length=50)
    connection_type = models.CharField(max_length=50)
    layout = models.CharField(max_length=20)

    
    