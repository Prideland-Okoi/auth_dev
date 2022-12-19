from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def homeview(request):
    return render(request, 'home/home.html')
