from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors, name='doctors'),
    path('AddDoc/',views.AddDoc,name='AddDoc'),
    path('removedoc/<int:id>/', views.remove_doc, name='remove-doc'),
    path('edit-doc/<int:id>/', views.edit_doc, name='edit-doc'),

]