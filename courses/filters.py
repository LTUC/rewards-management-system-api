import django_filters as filters
from .models import Rewads

class RewardsFilter(filters.FilterSet):
    id = filters.AllValuesFilter(field_name='owner__pk', lookup_expr='iexact')
  

    class Meta():
        model = Rewads
        fields=['id']

