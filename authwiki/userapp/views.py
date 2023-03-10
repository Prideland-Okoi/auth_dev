from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'home/login.html')
@login_required
def logout_user(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                #return redirect(register)
                return redirect(to='userapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                #return redirect(register)
                return redirect(to='userapp:register')
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                #return redirect('login_user')
                return redirect(to='userapp:login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            #return redirect(register)
            return redirect(to='userapp:register')
            

    else:
        return render(request, 'home/register.html')
@login_required
def profileview(request):
    return render(request, 'home/profile.html')

def forgotpassword(request):
    return render(request, 'home/forgot_password.html')

def emailverification(request):
    return render(request, 'home/email_verification.html')