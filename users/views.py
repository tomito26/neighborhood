from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,NeighborhoodUpdateForm
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        n_form = NeighborhoodUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and n_form.is_valid():
            u_form.save()
            p_form.save()
            n_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        n_form = NeighborhoodUpdateForm(instance=request.user)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'n_form' : n_form,
    }
    return render(request,'users/profile.html',context)