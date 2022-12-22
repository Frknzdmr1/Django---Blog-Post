from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Home Page </h1>")

def blog(request):
    return HttpResponse("<h1> Blog Page </h1>")

def blog_add(request):
    return HttpResponse("<h1> You can add a Blog </h1>")
