from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render (request,"index.html") 
def x (request):
    return render (request,"x.html") 