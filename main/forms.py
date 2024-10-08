from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class MakeProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "connection_type", "layout", "image"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)
    
    def clean_connection_type(self):
        connection_type = self.cleaned_data["connection_type"]
        return strip_tags(connection_type)
    
    def clean_layout(self):
        layout = self.cleaned_data["layout"]
        return strip_tags(layout)