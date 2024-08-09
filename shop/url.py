from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.index , name="shop" ),
    path("about/" , views.about , name="about"),
    path("productview/<int:myid>" , views.productview, name="about"),
    path("contact/" , views.contact_Form , name="contact"),
    
]
