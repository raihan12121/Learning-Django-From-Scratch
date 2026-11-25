from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/about', views.about, name='about'),
    
]