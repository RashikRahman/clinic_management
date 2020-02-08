from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('AddSer/',views.AddSer,name='AddServ'),
    path('removeservice/<int:id>/', views.remove_service, name='remove-service'),
    path('edit-service/<int:id>/', views.edit_service, name='edit-service'),
]