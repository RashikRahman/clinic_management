from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='uhome'),
    path('addappointment/', views.addappointment, name='addappointment'),
    path('seeappointment/', views.seeappointment, name='seeappointment'),
    path('edit-appointment/<int:id>/', views.edit_appointment, name='edit-appointment'),
    path('remove-appointment/<int:id>/', views.remove_appointment, name='remove-appointment'),


]