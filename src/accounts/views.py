from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import UserCreationForm


def user_creation_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponse('Hello world %s' % user.username)
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)                
                messages.success(request, 'Login successfuly')
                return redirect('home-page')
            elif not user.is_active:
                return HttpResponse('User is Inactive')
            else:
                messages.error(request, 'Invaild data!😡')
                return redirect('account-login')
    
    context = {}
    return render(request, 'accounts/login.html', context)


def user_logout_view(request):
    
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Successfuly Logout!')
        return redirect('home-page')
    
    context = {}
    return render(request,'accounts/login.html', context)