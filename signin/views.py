# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

def signin(request):
  c = Context({"datos": ["Signin", "Alexandra", "Hoy"]}) 
  return render(request, "signin/templates/signin.html", c)
 
