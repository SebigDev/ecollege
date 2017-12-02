from django.contrib import auth, messages

from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('success_reg')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')
