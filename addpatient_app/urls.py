from django.urls import path
from . import views

urlpatterns = [
    path('', views.addpatient, name='addpatient'),
    path('addpatients/', views.addpatients, name='AddPatients'),
    path('removepatient/<int:id>/', views.remove_patient, name='remove-patient'),
    path('edit-patient/<int:id>/', views.edit_patient, name='edit-patient'),
]