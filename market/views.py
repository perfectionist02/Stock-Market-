from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Stock

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    return render(request,'market/homepage.html')

def stocks(request):
    stockslist = Stock.objects.orderby('symbol')
    context = {'stockslist':stockslist}
    return render(request, 'market/stocks.html',context}
    
def register(request):
    
    
    
    
def loginpage(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home')
        else:
            HttpResponseRedirect(

# Create your views here.
