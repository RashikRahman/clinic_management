import django_filters
from .models import appointment

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = appointment
        feilds = '__all__'
        exclude = ['msg','ltd']
