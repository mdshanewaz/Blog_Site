from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

# Create your views here.

def signup(request):
    form = UserCreationForm()
    registered = False

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {
        "form" : form,
        "registered" : registered,
    }

    return render(request, 'Login_App/signup.html', context=dict)

def login_page(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
    return render(request, 'Login_App/login.html', context={'form':form})

