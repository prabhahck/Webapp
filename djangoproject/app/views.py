from django.http.response import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse("Welcome to the site")
    return render(request, 'home.html')