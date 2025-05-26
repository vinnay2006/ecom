from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render( request,"shop/index.htm")

def about(request):
    return HttpResponse("we are at abouts")
def contact(request):
    return HttpResponse("we are at abouts")
def tracker(request):
    return HttpResponse("we are at abouts")
def search(request):
    return HttpResponse("we are at abouts")
def prodView(request):
    return HttpResponse("we are at abouts")
def checkout(request):
    return HttpResponse("we are at abouts")


