from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login ,logout
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    return render(request,'market/main.html')

def stocks(request):
    #stockslist = Stock.objects.all()
    name = request.GET['name']
    print(name)
    stockslist = Stock.objects.filter(symbol__startswith=name)
    context = {'stockslist':stockslist}
    return render(request, 'market/stock.html',context)
    
    
def portfolio(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            customer = User.objects.get(username=request.user.username).customers
            Portfoliolist = Portfolio.objects.filter(owner__id=customer.id)
            return render(request,'market/portfolio.html',{'stockslist':Portfoliolist,'balance':customer.balance})        
    else:
        return HttpResponseRedirect('../login')    

def logoutaction(request):
    logout(request)
    return HttpResponseRedirect('../homepage')

def transact(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            return render(request,'market/transact.html')
        elif request.method=="POST":
            symbol=request.POST['symbol'].upper()
            volume=int(request.POST['volume'])
            customer=User.objects.get(username=request.user.username).customers
            if request.POST['choice']=="buy":
                customer.buy(symbol,volume)
            elif request.POST['choice']=="sell":
                customer.sell(symbol,volume)
            return HttpResponseRedirect("../portfolio")
          
    else:
        return HttpResponseRedirect('../login')
    
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("../homepage")
    if request.method=="GET":
        return render(request,'market/register.html',{'error':""})
    elif request.method=="POST":
        username = request.POST['uname']
        password = request.POST['password']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        try:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
            user.save()
            return HttpResponseRedirect('../login')
        except:
            return render(request,'market/login.html',{"error":e})    
    
    
def loginaction(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("../homepage")
    if request.method=="GET":
        return render(request,'market/login.html',{'error':""})    
    elif request.method=="POST":
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../portfolio/')
            else:
                return render(request,'market/login.html',{'error':"The user account is inactive"})
        else:
            return render(request,'market/login.html',{'error':"Please enter correct username/password"})
