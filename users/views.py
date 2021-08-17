from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls.base import reverse
from .forms import CustomUserCreationForm

def index(request):
    #! view function in django should not return string just http response.
    if request.user.is_authenticated:
        return redirect(reverse('personalDiary:home'))
    return redirect(reverse('users:login'))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('personalDiary:home'))
        return render(request, 'users/register.html', context={'form': form})
    form = CustomUserCreationForm()
    return render(request, 'users/register.html', context={'form': form})
