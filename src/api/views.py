from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from images.models import Image

from .serializers import ImageSerializer
from . import services


@api_view(['GET'])
def list_all_image_view(request):
    # Queries params
    api_token = request.GET.get('api_key', None)
    usernames = request.GET.getlist('users') or None
    tags = request.GET.getlist('tags') or None
    
    qs = Image.objects.filter(active=True)
    
    if usernames is not None:
        qs = qs.filter(user__username__in=usernames)
    
    if tags is not None:
        qs = qs.filter(tags__name__in=tags)
    token, is_vaild = services.verify_token(api_token)
    
    serializer = ImageSerializer(qs, many=True)
    
    if not is_vaild:
        return Response({'Error': 'An Error Occured'}, status=404)
    
    return Response(serializer.data)
