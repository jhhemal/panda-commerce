from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import CategoryCreationForm, ProductCreationForm
from .models import Category, Product
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    ctx = {
        'categories' : categories,
        'products' : products,
    }
    return render(request, 'ecommerce/index.html', context=ctx)

class CategoryCreateView(CreateView):
    form_class = CategoryCreationForm
    template_name = 'ecommerce/create_category.html'
    success_url = reverse_lazy('home')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreationForm
    success_url = reverse_lazy('home')

class ProductCreateView(CreateView):
    form_class = ProductCreationForm
    template_name = 'ecommerce/create_product.html'
    success_url = reverse_lazy('home')
