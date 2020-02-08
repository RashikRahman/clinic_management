from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='s'),
    path('login/', views.logins, name='login'),
    path('lougts/',views.lougts,name='logout'),
]