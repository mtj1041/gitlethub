from django.shortcuts import render

from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.shortcuts import render
from .forms import UploadFileForm

from .models import File

import forms
import os
import models
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        files = File.objects.filter(user_belongs=request.user.get_username(), commit_id='1')
    
    commit_dict = {}
    for i in files:
        print(i.commit_id)
        if i.commit_id in commit_dict.keys():
            commit_dict[i.commit_id].append(i)
        else:
            commit_dict[i.commit_id] = [i]
            
    #files.filter(commit_id='2')
    return render(request, 'hub/index.html', {"files":files, "keys":commit_dict.keys()})

def panel(request, userid):
    return render(request, 'hub/index.html', {"userid":userid})

def upload_file(request):
    if '&' in request.get_full_path().split("/")[-1]: # remote user interaction
        params = request.get_full_path().split("/")[-1].split("&")
        username = params[0]
        password = params[1]
        commit_id = params[2]
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['docfile']
            model_file = File(file=file, name='regfile', user_belongs=request.user.get_username(), commit_id='2')
            model_file.save()
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'hub/upload.html', {'form': form})

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
    if request.get_full_path().split("/")[-1] != "" and request.get_full_path().split("/")[-1] != "login": # handling remote connections
        params = request.get_full_path().split("/")[-1].split("&")
        username = params[0]
        password = params[1]
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
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

def repo(request, user):
    logged_user = request.user.username
    
    return HttpResponse("User: " + user + " Logged in user: " + logged_user)