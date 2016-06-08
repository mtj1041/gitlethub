from django.shortcuts import render

from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse("Hello!")

def panel(request, userid):
    return render(request, 'hub/index.html', {"userid":userid})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/hub/")
    else:
        form = UserCreationForm()
    return render(request, "hub/register.html", {
        'form': form,
    })