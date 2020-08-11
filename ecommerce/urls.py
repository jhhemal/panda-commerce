from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('category/create/', views.CategoryCreateView.as_view(), name='create-category'),
    path('product/create/', views.ProductCreateView.as_view(), name='create-product')
]
