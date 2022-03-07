from django.shortcuts import render
from django.http import HttpResponse


def return_page(request):
    return render(request, "base.html")


def example(self):
    return HttpResponse("Hola")


def example2(self):
    return HttpResponse("Cesar Joto")

# Create your views here.
