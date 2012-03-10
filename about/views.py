# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

def about(request):
  c = Context({"datos": ["About", "Alexandra Rivero", "08-MAR-2011"]}) 
  return render(request, "about/templates/about.html", c)