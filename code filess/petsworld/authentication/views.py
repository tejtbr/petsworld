from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"authentication/hhome.html")

def singup(request):
    return render(request,"authentication/singup.html")


def signin(request):
        return render(request,"authentication/signin.html")


def signout(request):
    pass