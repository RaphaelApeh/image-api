import django_filters

from images.models import Image

class ImageFilterSet(django_filters.FilterSet):

    tags = django_filters.CharFilter(field_name='tags__name', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    class Meta:
        model = Image
        fields = ['name', 'username', 'slug', 'tags', 'timestamp']