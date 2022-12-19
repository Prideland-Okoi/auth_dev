from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def homeview(request):
    return render(request, 'home/home.html')

def communityview(request):
    return render(request, 'home/communitypage.html')

def communityview_b(request):
    return render(request, 'home/communitypage2.html')

def communityview_c(request):
    return render(request, 'home/communitypage3.html')

def feedbackview(request):
    return render(request, 'home/feedback.html')

def errorview(request):
    return render(request, 'home/error.html')

def dashboardview(request):
    return render(request, 'home/dashboard.html')

