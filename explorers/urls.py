from django.urls import path
from explorers import views

#assemblies 

urlpatterns = [
    path('explorers/', views.AssemblyList.as_view()),
]
