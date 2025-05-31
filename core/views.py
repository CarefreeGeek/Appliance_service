from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from core.middlewares import auth, guest
# Create your views here.

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render (request,'auth/user_dashboard.html')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return render (request,'core/dashboard.html')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@auth
def dashboard_view(request):

    return render(request, 'auth/user_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')




def mac_dashboard(request):
    return render(request, 'auth/mac_dashboard.html')


def user_dashboard(request):
    return render(request, 'auth/user_dashboard.html')