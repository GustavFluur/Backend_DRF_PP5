from django.urls import path
from explorers import views



urlpatterns = [
    path('explorers/', views.AssemblyList.as_view()),
]
