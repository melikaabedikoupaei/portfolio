"""
URL configuration for Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path("Data_visualization_project/", Data_visualization_project, name="Data_visualization_project"),
    path("Machine_learning_project/", Machine_learning_project, name="Machine_learning_project"),
    path("Customer_Churn_project/", Customer_Churn_project, name="Customer_Churn_project"),
    path("JobMatchAI_project/", JobMatchAI_project, name="JobMatchAI_project"),
    path("roadmap/", roadmap, name="roadmap"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

