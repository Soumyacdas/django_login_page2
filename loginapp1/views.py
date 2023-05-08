from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def Homepage(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect(LoginPage)
    
@never_cache
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Username/Password")
    return render(request,'signin.html')
@never_cache
def SignupPage(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            return HttpResponse("Passwords are not same!!!")
        else:
            new_user=User.objects.create_user(username,email,password)
            new_user.save()
            return redirect('login')

        
    return render(request,'signup.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')
