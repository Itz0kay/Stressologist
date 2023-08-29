from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import auth, messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required

from Accounts.forms import *
from Programs.models import ProgramLog
from Tests.models import Result
from datetime import date


# Create your views here.

# New views starts from here
def index_page(request):
    context = {
        'page':'index'
    }
    return render(request, 'Accounts/index.html', context)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Accounts:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'Accounts/login.html', context)

def user_register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("Accounts:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUserForm()
    
    context = {
        'form': form
    }
    return render(request, 'Accounts/register.html', context)

def aboutus(request):
    context = {}
    return render(request, 'Accounts/aboutus.html', context)

def image(request):
    context = {}
    return render(request, 'Accounts/captureImg.html', context)


@login_required
def home(request):
    all_results = list(Result.objects.filter(user=request.user).values())
    all_programs = list(ProgramLog.objects.filter(user=request.user).values())
    if len(all_results) != 0:
        total_days_spent = int((date.today() - all_results[0]['cwhen']).total_seconds() / (24 * 60 * 60))

        total = 0
        count = 0
        for i in all_results:
            count += 1
            total += i["stresslevel"]
        total //= count
    else:
        total_days_spent = 0
        total = 0
    context = {
        'total_days_spent':total_days_spent,
        'total_stress':total,
        'programs':len(all_programs),
        'page':'home',
    }
    return render(request, 'Accounts/home.html', context)

@login_required
def user_logout(request):
    auth.logout(request)
    messages.get_messages(request).used=True
    messages.success(request,'Logged Out Successfully!')
    return redirect('Accounts:login')




def inptest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Accounts:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'Accounts/inptest.html', context)


