# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

def help(request):
  c = Context({"datos": ["Help", "Alexandra", "Hoy"]}) 
  return render(request, "help/templates/help.html", c)