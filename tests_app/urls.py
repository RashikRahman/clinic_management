from django.urls import path
from . import views

urlpatterns = [
    path('', views.tests, name='tests'),
    path('AddTest/', views.AddTest, name='AddTst'),
    path('removetest/<int:id>/', views.remove_test, name='remove-test'),
    path('edit-test/<int:id>/', views.edit_test, name='edit-test'),
]