from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

from images.models import Image

def verify_token(token):
    if token is None:
        raise ValidationError('API Token must not be None') 
    try:
        auth_token = Token.objects.get(key=token)
        return auth_token, True
    except Token.DoesNotExist:
        return None, False
    

def get_user_from_token():
    ...