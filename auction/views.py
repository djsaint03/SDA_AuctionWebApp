from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
from .forms import CreateUserForm



def loginpage(request):
    return render(request, 'accounts/login.html')

def registerpage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username") #to get username
            messages.success(request, "Account created for ", + user)
            return redirect("login")


    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request,"products.html")