import django_filters
from professionals.models import Service
from django_filters import CharFilter

class ServiceFilter(django_filters.FilterSet):
  service_contains_location = CharFilter(field_name='service_location', lookup_expr='icontains' )
  service_contains_name = CharFilter(field_name='service_name', lookup_expr='icontains' )

  class Meta:
    model = Service
    fields = ''

