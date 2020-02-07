from django.urls import path
from . import views

urlpatterns = [
    path('', views.department, name='departments'),
    path('AddDept/',views.AddDept,name='AddDept'),
]