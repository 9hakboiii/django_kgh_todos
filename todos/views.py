from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# dev_1
def home(request):
    return render(request, "home.html")
