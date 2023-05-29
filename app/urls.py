from .models import Student
from django.urls import path


urlpatterns=[
    path("student/",Student)
]