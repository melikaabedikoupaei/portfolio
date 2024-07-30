from django.shortcuts import render
from django.http import HttpResponse
import requests

def index (request):
    return render (request,"index.html") 
def Data_visualization_project (request):
    return render (request,"Data_visualization_project.html") 
def roadmap(request):
    return render (request,"roadmap.html") 
def proxy_audio(request):
    response = requests.get('https://drive.google.com/uc?export=download&id=1YvuC0Ivn5QCq0h8sAdOoyFi11mnhwprz')
    return HttpResponse(response.content, content_type='audio/mpeg')