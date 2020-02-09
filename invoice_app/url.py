from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('AddInvc/', views.AddInvc, name='AddInvc'),
    path('removeinvoice/<int:id>/', views.remove_invoice, name='remove-invoice'),
    path('edit-invoice/<int:id>/', views.edit_invoice, name='edit-invoice'),
    path('printinvoice/<int:id>/', views.print_invoice, name='print_invoice'),
]