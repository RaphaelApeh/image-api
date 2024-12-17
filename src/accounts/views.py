from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate

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
            if user is not None:
                login(request, user)
                
                messages.success(request, 'Login successfuly')
                return HttpResponse(f'{username}')
    
    context = {}
    return render(request, 'accounts/login.html', context)