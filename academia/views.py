from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from academia.models import Photos

def index(request):

    photos = Photos.objects.all()
    return render(request, 'academia/index.html', {"cards":photos})

def contact(request, photo_id):
    photo = get_object_or_404(Photos, pk=photo_id)
    return render(request, 'academia/contact.html', {"photo": photo})

# Create your views here.
