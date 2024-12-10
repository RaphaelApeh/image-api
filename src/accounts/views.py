from django.shortcuts import render

from .forms import UserCreationForm


def user_creation_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def user_login_view(request):
    if request.method == 'POST':
        ...
    context = {}
    return render(request, 'accounts/login.html', context)