from django.shortcuts import render
from django.http import HttpResponse
import requests

def index (request):
    return render (request,"index.html") 
def Data_visualization_project (request):
    return render (request,"Data_visualization_project.html") 
def roadmap(request):
    return render (request,"roadmap.html") 
