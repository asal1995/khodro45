from django_filters.rest_framework import FilterSet
from khodro45_app.models import Brand


class BrandFilterSet(FilterSet):
    class Meta:
        model = Brand
        fields = {
            'title': ['icontains'],



        }
