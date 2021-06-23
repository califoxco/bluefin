import django_filters
from django_filters import CharFilter, RangeFilter
from django.db.models import ImageField
from .models import Property


# ------------------------------------ Filter ------------------------------------
# Description: Custom django-filter for filtering homes
# Parameter: django_filter
# --------------------------------------------------------------------------------
class PropertyFilter(django_filters.FilterSet):
    city = CharFilter(field_name='city', lookup_expr='icontains')
    price = RangeFilter()

    class Meta:
        model = Property
        fields = ['price', 'number_bedroom', 'property_type']
        filter_overrides = {
            ImageField: {
                'filter_class': django_filters.CharFilter,
            }
        }
