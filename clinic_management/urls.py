from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointment_app.urls')),
    path('login/', include('login_app.urls')),
    path('patients/', include('patient_app.urls')),
    path('department/', include('department_app.urls')),
    path('dashboard/', include('dashboard_app.urls')),
    path('pro/', include('PRO_app.urls')),
    path('services/', include('services_app.urls')),
    path('doctors/', include('doctor_app.urls')),
    path('tests/', include('tests_app.urls')),
    path('addpatient/',include('addpatient_app.urls')),
    path('invoice/',include('invoice_app.url'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

