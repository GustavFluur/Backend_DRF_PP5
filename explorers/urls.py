from django.urls import path
from explorers import views


urlpatterns = [
    path('explorers/', views.AssemblyList.as_view()),
    path('explorers/<int:pk>/', views.AssemblyDetail.as_view()),
]
