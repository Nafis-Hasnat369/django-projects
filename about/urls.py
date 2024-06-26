from django.urls import path
from about import views

urlpatterns = [
    path('', views.about, name="about"),
    path('teacher/', views.teachers_info, name="teacher"),
]
