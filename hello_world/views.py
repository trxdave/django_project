from django.shortcuts import render
from django.http import HttpResponse
from hello_world import views as index_views

# Create your views here.


def about_me(request):
    return HttpResponse("This would be the about page")
