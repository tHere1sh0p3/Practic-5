from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    return HttpResponse("<h1>Главная</h1>")
 
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def hello(request):
    return render(request, "home.html")

