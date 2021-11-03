import django_filters as filters
from .models import Rewad

class RewardsFilter(filters.FilterSet):
    id = filters.AllValuesFilter(field_name='owner__pk', lookup_expr='iexact')
  

    class Meta():
        model = Rewad
        fields=['id']

