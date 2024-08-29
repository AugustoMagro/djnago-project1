from django.urls import path
from academia.views import index

urlpatterns = [
    path('', index),
]