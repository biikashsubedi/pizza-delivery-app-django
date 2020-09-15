from django.contrib import admin
from django.urls import path
from .views import adminloginview, adminhomepage, authenicationadmin, adminlogout, addpizza, deletepizza

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthencicate/', authenicationadmin),
    path('adminlogout/', adminlogout),
    path('admin/homepage', adminhomepage, name='adminhomepage'),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
]
