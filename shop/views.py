from django.shortcuts import render
from django.http import HttpResponse
from  .models import Product,Contact
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
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')
        print(name,email,subject,message)
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render( request,"shop/contact.htm")
def tracker(request):
    return render( request,"shop/tracker.htm")
def search(request):
    return render( request,"shop/search.htm")
def prodView(request,myid):
    product=Product.objects.filter(id=myid)
    return render( request,"shop/prodView.htm",{'product':product[0]})
def checkout(request):
    return render( request,"shop/checkout.htm")


