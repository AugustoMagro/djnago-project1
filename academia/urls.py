from django.urls import path
from academia.views import index, contact

urlpatterns = [
    path('', index),
    path('contact/', contact, name='contact')
]