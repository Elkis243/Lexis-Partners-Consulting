from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('favicon.ico', favicon_view, name='favicon'),
]
