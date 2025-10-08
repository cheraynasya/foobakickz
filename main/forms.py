from django.forms import ModelForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

TAILWIND_CLASS = 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:border-tealEgg focus:ring-tealEgg'

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': TAILWIND_CLASS})
            
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': TAILWIND_CLASS})
            
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock"]