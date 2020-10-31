from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisterForm

#   Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You are now able to login')
            return redirect('login')
    else: 
        form =UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

def home(request):
    return render(request,'home.html')