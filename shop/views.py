from django.shortcuts import render
from django.http import HttpResponse
from  .models import Product
from math import ceil
def index(request):
    products=Product.objects.all()
    print(products)
    #params={'no_of_slides':nslides,'range':range(1,len(products)),'product':products}

    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides= n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])

    params={'allprods':allprods}
    return render( request,"shop/index.htm",params)
    

def about(request):
    return render( request,"shop/about.htm")
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


