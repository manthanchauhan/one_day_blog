from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        print('hi')
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_url')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Create your views here.
