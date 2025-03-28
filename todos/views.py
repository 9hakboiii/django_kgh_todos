from django.shortcuts import render
from django.http import HttpResponse


# dev_1
def home(request):
    return render(request, "home.html")
