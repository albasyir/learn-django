from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>This is the products app homepage</h1>")


def new(request):
    return HttpResponse("<h1>This is the products app new page</h1>")
