from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'academia/index.html')

def contact(request):
    return render(request, 'academia/contact.html')

# Create your views here.
