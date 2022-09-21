from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def myprogram(request):
    return render(request, 'myprogram.html')
    
def shoppinglist(request):
    return render(request, 'shoppinglist.html')

def recipes(request):
    return render(request, 'recipes.html')

def sports(request):
    return render(request, 'sports.html')

def motivation(request):
    return render(request, 'motivation.html')

def performance(request):
    return render(request, 'performance.html')

def food(request):
    return render(request, 'food.html')

def training(request):
    return render(request, 'training.html')

def cardio(request):
    return render(request, 'cardio.html')

def gym(request):
    return render(request, 'gym-sessions.html')
    
def home_session(request):
    return render(request, 'home-session.html')
   


def signup_user(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account has been created successfully.')
            return HttpResponseRedirect('login')
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{'form':fm})


def login_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            email=request.POST['email']
            password = request.POST['password']
            if register.objects.filter(email=email).exists():
                user = register.objects.get(email=email)
                print(user,'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
                if register.objects.filter(password=password).exists():
                    password_get = str(register.objects.get(password=password))
                    print(password_get)
                    user_last = authenticate(username=user, password=password_get)
                    if user is not None:
                        login(request, user)
                        return render(request,'profile.html')         
        else:
            pass
        return render(request,'profile.html')
    else:
        messages.success(request,'You are already login')
        return HttpResponseRedirect('/')
        


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')