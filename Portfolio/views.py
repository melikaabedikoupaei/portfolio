from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render (request,"index.html") 
def Data_visualization_project (request):
    return render (request,"Data_visualization_project.html") 
def Machine_learning_project (request):
    return render (request,"Machine_learning_project.html") 
def Customer_Churn_project (request):
    return render (request,"Customer_Churn_project.html") 

def JobMatchAI_project (request):
    return render (request,"JobMatchAI_project.html") 

def roadmap(request):
    return render (request,"roadmap.html") 
