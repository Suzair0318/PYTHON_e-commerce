
from django.shortcuts import render
from .models import product , contact
# Create your views here.

def index(request):
    products = product.objects.all()
    # print(products[0].product_name)
    category = product.objects.values('product_category')
    def fil(n):
          return n['product_category']
    
    unique_category = list(map( fil , category))
    filt = set(unique_category)
    
    params = { 'database_products' : products , 'filt_category' : filt }
    return render( request , 'shop/index.html' , params)

def about(request):
    return render( request , 'shop/about.html')

def productview(request , id):
     print(id)
     return render( request , 'shop/productview.html' )

def contact_Form(request):
     if request.method == "POST":

          name = request.POST.get("name", "")
          email = request.POST.get("email", "")
          phone = request.POST.get("phone", "")
          address = request.POST.get("address", "")

          db_form_contact = contact( user_name=name , user_email=email , user_phone=phone , user_adddres=address )
          db_form_contact.save()
        
     

     return render( request , 'shop/contact.html' )