from django.views.decorators.csrf import csrf_exempt

from rest_framework import parsers, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from images.models import Image

from .serializers import ImageSerializer
from . import services, filters


@api_view(['GET'])
def list_all_image_view(request):
    # Queries params
    api_token = request.GET.get('api_key')

    queryset = Image.objects.filter(active=True)
    qs_filter = filters.ImageFilterSet(request.GET, queryset=queryset)
    # Pagination
    paginator = services.ImagePagePaginator()
    token, is_vaild = services.verify_token(api_token)
    qs = qs_filter.qs
    image_ = paginator.paginate_queryset(qs, request)
    serializer = ImageSerializer(image_, many=True)
    
    if not is_vaild:
        return Response({'Error': 'An Error Occured'}, status=404)
    
    return paginator.get_paginated_response(serializer.data)
