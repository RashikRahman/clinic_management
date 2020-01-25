from django.urls import path
from . import views

urlpatterns=[
    path('',views.show,name='bdpro'),
    path('addstudent/', views.addstudent,name='addd')

]
