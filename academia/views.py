from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from academia.models import Photos

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if "search" in request.GET:
        name_search = request.GET['search']
        if name_search is not None:
            photos = Photos.objects.order_by("date_photo").filter(name__icontains=name_search, visible=True)
    
    else:
        photos = Photos.objects.order_by("date_photo").filter(visible=True)
        

    return render(request, 'academia/index.html', {"cards":photos})
        
def contact(request, photo_id):
    if not request.user.is_authenticated:
        return redirect('login')

    photo = get_object_or_404(Photos, pk=photo_id)
    return render(request, 'academia/contact.html', {"photo": photo})

# Create your views here.
