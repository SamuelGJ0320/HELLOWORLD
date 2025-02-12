from django.urls import path
from .views import HomePageView, AboutPageView, ProductShowView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductShowView.as_view(), name='products'),  # Aquí defines /products/
]
