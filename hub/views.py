from django.shortcuts import render

from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import auth

import forms

# Create your views here.

def index(request):
    return render(request, 'hub/index.html', {"userid":30})

def panel(request, userid):
    return render(request, 'hub/index.html', {"userid":userid})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "hub/register.html", {
        'form': form,
    })

def login(request):
    if request.get_full_path().split("/")[-1] != "": # handling remote connections
        params = request.get_full_path().split("/")[-1].split("&")
        username = params[0]
        password = params[1]
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            return HttpResponse("Remote credentials correct")
        else:
            return HttpResponse("Remote credentials incorrect")
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print("USERNAME: " + username)
        print("PASSWORD: " + password)
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
            auth.login(request, user)
        # Redirect to a success page.
            return HttpResponseRedirect("/success")
            
            #return render(request, 'hub/account/success.html')
            
        else:
            # Show an error page
            return HttpResponseRedirect("/failure")
    else:
        form = forms.LoginForm()
        return render(request, "hub/login.html", {"form":form})

def logout(request):
    if request.user:
        auth.logout(request)
        return HttpResponse("You have successfully logged out.")
    else:
        return HttpResponse("You are not logged in! Please login first.")

def success(request):
    return render(request, 'hub/account/success.html', {"user":request.user})

def failure(request):
    return render(request, 'hub/account/failure.html')
    
