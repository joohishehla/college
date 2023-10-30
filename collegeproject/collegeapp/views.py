from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "index.html")


def newpage(request):
    return render(request, "newpage.html")


def form(request):
    if request.method == 'POST':
        messages.info(request, "Successfully Submitted")
    return render(request, "Form.html", )


def register(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        Password1 = request.POST['Password1']

        if Password == Password1:
            if User.objects.filter(username=Username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=Username, password=Password)
                user.save();
            return redirect('login')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
    #
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        user = auth.authenticate(username=Username, password=Password)

        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
