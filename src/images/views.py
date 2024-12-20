from django.shortcuts import render

from api.filters import ImageFilterSet
from .models import Image


def image_display_view(request):
    qs = Image.objects.filter(active=True)
    
    filters = ImageFilterSet(request.GET, queryset=Image.objects.filter(active=True))
    qs = filters.qs
    context = {'queryset':qs}
    return render(request, 'images/base.html', context)