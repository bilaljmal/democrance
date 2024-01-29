from django_filters import rest_framework as filters

from .models import Customers


class CustomerFilter(filters.FilterSet):

    class Meta:
        model = Customers
        fields = ['first_name','last_name','dob','policies__type']
