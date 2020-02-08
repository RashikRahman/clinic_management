from django.urls import path
from . import views

urlpatterns = [
    path('', views.addpatient, name='addpatient'),
    path('addpatients/', views.addpatients, name='AddPatients'),
]