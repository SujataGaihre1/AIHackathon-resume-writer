from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at resume Upload page")


def view_name(request):
    return render(request, 'app_name.html', {})
