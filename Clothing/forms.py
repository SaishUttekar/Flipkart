from django import forms    
from .models import CloProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = CloProduct
        fields = '__all__'  