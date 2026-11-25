from django.urls import path
from shop import views

urlpatterns =[
    path('', views.home, name='shop-home'),
    path('product/', views.products, name='shop-product'),
]