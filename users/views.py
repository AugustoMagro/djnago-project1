from django.shortcuts import render, redirect
from users.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            user = form["user"].value()
            password = form["password"].value()
        
        user = auth.authenticate(
             request,
             username=user,
             password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login with success!")
            return redirect('')
        else:
            messages.error(request, "Login error!")
            return redirect('login')

    return render(request, "users/login.html", {"form": form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)
        
        if form.is_valid():
            if form["password_1"].value() != form["password_2"].value():
                        return redirect('register')
            
            name = form["name"].value()
            email = form["email"].value()
            password_1 = form["password_1"].value()

            if User.objects.filter(username=name).exists():
                return redirect('register')
            
            user = User.objects.create_superuser(
                 username=name,
                 email=email,
                 password=password_1
            )
            user.save()
            return redirect('login')

    return render(request, "users/register.html", {"form":form})

def logout(request):
     auth.logout(request)
     messages.success(request, "Logout with success!")
     return redirect('login')