from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel


def adminloginview(request):
    return render(request, 'pizzaapp/adminlogin.html')


def adminhomepage(request):
    return render(request, 'pizzaapp/adminhomepage.html', {'pizzas': PizzaModel.objects.all()})


def authenicationadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # if user exist
    if user is not None and user.username == 'admin':
        login(request, user)
        return redirect('adminhomepage')

    # if user not exist
    if user is None:
        messages.add_message(request, messages.ERROR, 'Invalid Detail, Contact Admin First')
        return redirect('adminloginpage')


def adminlogout(request):
    logout(request)
    messages.add_message(request, messages.ERROR, 'You are successfully Logout')
    return redirect('adminloginpage')


def addpizza(request):
    name = request.POST['name']
    price = request.POST['price']
    PizzaModel(name=name, price=price).save()
    return redirect('adminhomepage')

def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')

def homepage(request):
    return render(request, 'pizzaapp/homepage.html')
