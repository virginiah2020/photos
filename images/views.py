from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image,Location
# Create your views here.
def images(request):

    images = Image.objects.all()
    return render(request, 'images.html', {'images': images[::-1]})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_images)

        return render(request,'images/search_results.html',{"message":message,"images":searched_images})

    else:
        message="You haven't searched for any term"
        return render(request,'images/search_results.html',{"message":message})