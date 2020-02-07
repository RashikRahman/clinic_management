from django.urls import path
from . import views

urlpatterns = [
    path('', views.tests, name='tests'),
    path('AddTest/', views.AddTest, name='AddTst'),
]