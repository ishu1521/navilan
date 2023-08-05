from django.shortcuts import render
from cartApp.models import Product
# Create your views here.
def funcHome(request):
    elist=Product.objects.all()
    return render(request,'htmlpages/home.html',{'elist':elist})
def funcElectronic(request):
    elist=Product.objects.all()
    return render(request,'htmlpages/electronics.html',{'elist':elist})
def funcFashion(request):
     elist=Product.objects.all()
     return render(request,'htmlpages/fashion.html',{'elist':elist})
def funcGroceries(request):
     elist=Product.objects.all()
     return render(request,'htmlpages/groceries.html',{'elist':elist})