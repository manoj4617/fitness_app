from django.contrib import messages
from django.contrib.auth import authenticate, login , logout 
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import *



def index(request):
    return render(request , 'fit/home.html', {'text':"Hello "})

def login_get(request):
    return render(request,'fit/login.html')

def signup_get(request):
    return render(request,'fit/signup.html')

def logout_get(request):
    logout(request)
    print(User.first_name,"logged out")
    return render(request,'fit/home.html')

def Signup(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['uname']
        p = dic['con_pass']
        mob = dic['pno']
        f = dic['fname']
        l = dic['lname']
        email = dic['email']
        age = dic['age']
        gender = dic['gender']
        img = request.FILES['pic']
        weight = dic['weight']
        height = dic['height']
        userdata = User.objects.filter(username=u)
        if userdata:
            context = {
                "message":"User already exists"
            }
            return render(request,'fit/login.html', context)
        else:
            user = User.objects.create_user(first_name=f, last_name=l, username=u, password=p, email=email)
            User_details.objects.create(user=user, mobile_no=mob, profile_image=img, age=age, gender=gender,
                                        weight=weight, heigth=height)
            context = {
                "message":"Account created! Login"
            }
            return render(request,'fit/login.html', context)
    return render(request, 'fit/signup.html')

def Login(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['username']
        p = dic['pass']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            #return redirect('home')
            userLoggedIn = Goals.objects.filter(user=request.user)
            #print(userLoggedIn)
           
            context = {
                "goals" : userLoggedIn
            }
            #print(userLoggedIn)
            return render(request,'fit/main_page.html', context)
        else:
            messages.error(request, 'User not found')
            context = {
                "message": "User not found"
            }
            return render(request,'fit/login.html',context)

    return render(request, 'fit/login.html')

#def account(request,id):
   #uid = int(id)
    
def add_task(request):
    if request.method == "POST":
        dec = request.POST
        task = dec['goal']
        fromDate = dec['start-date']
        endDate = dec['end-date']
        goal = Goals.objects.create(user=request.user,Task_date=fromDate,Due_date=endDate,task_name = task)
        goal.save()
        userLoggedIn = Goals.objects.filter(user=request.user)
        context = {
            "goals" : userLoggedIn
        }
        print(userLoggedIn)
        return render(request,'fit/main_page.html', context)

def Diet(request):
    return render(request,"fit/diet.html")