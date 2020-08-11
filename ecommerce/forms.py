from django import forms
from .models import Category, Product

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : "Enter Category name"
            })
        }

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'categories', 'image']

        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : "Enter Product name"
            }),
            'description' : forms.Textarea(attrs={
                'placeholder' : "Enter Product description",
                'rows' : 5
            }),
            'price' : forms.NumberInput(attrs={
                'placeholder' : "Enter Product price"
            }),
        }
    
