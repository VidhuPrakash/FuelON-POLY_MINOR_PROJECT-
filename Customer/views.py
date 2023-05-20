from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Fuel,category,order_data,KeralaHub

class index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/index.html')
    
class About(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/about.html')

class hub(View):
    def get(self,request,*args,**kwargs):
        Customer=KeralaHub.objects.all()
        return render(request,'customer/hub.html',{'Customer':Customer})
    
class Order(View):
    def get(self,request,*args,**kwargs):
       Customer=Fuel.objects.all()
      
       return render(request,'customer/order.html',{'Customer':Customer})

        
    
    def post(self,request,*args,**kwargs):
      
        return render(request,'customer/order_confirmation.html')
class Save(View):
      def post(self,request,*args,**kwargs):
       if request.method=="POST":
           customer_name=request.POST.get('customer_name')
           phone=request.POST.get('phone')
           category=request.POST.get('category')
           location=request.POST.get('location')
           quantity=request.POST.get('quantity')
           en=order_data(customer_name=customer_name,phone=phone,location=location,quantity=quantity,category=category)
           en.save()

           
       return render(request,'customer/save_enque.html')
class OrderData(View):
    def get(self,request,*args,**kwargs):
        Customer=order_data.objects.all()
        return render(request,'customer/orderdetails.html',{'Customer':Customer})
         
    
    

