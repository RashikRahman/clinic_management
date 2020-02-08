from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients, name='patients'),
    path('prescribe/<int:id>/', views.prescribe_view, name='prescribe'),
]