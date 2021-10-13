from django.shortcuts import render
from django.http import HttpResponse, response
from .models import ToDoList , Items

# Create your views here.

def index(request,names):
    ls = ToDoList.objects.get(names = names)
    items = ls.items_set.get(id=1)
    #return HttpResponse("<h1>%s</h1>" %(ls.names))
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})
