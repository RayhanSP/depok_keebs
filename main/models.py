from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()           
    description = models.TextField()
    category = models.CharField(max_length=50)
    connection_type = models.CharField(max_length=50)
    layout = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)


    