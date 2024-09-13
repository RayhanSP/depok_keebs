from django.forms import ModelForm
from main.models import Product

class MakeProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "connection_type", "layout"]