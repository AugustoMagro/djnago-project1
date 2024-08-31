from django.urls import path
from academia.views import index, contact

urlpatterns = [
    path('', index, name=''),
    path('contact/<int:photo_id>', contact, name='contact')
]