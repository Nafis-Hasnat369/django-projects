from django.urls import path
from about import views

urlpatterns = [
    path('', views.about, name="about"),
    path('teacher/', views.teachers_info, name="teacher"),
    path('form/', views.show_forms_data, name="form"),
]
# Use forms to ensure the changes