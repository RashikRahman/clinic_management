from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors, name='doctors'),
    path('AddDoc/',views.AddDoc,name='AddDoc'),

]