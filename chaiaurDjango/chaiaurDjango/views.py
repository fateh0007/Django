from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, welcome to Chai aur Django home page!")
    return render(request, "website/index.html")

def about(request):
    return HttpResponse("Hello, welcome to Chai aur Django about page!")

def contact(request):
    return HttpResponse("Hello, welcome to Chai aur Django contact page!")