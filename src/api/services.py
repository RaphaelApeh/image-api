import time
import typing

from django.utils import timezone

from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token

from .models import UserToken
from images.models import Image


class ImagePagePaginator(PageNumberPagination):
    page_size = 1


def verify_token(token: str):
    if token is None:
        raise ValueError('API Token must not be None') 
    try:
        auth_token = Token.objects.get(key=token)
        return auth_token, True
    except Token.DoesNotExist:
        return None, False
    

def get_user_from_token():
    ...

def user_token(token: typing.Type[Token]):

    token_key = token.key
    user = token.user
    _user_token = UserToken.objects.filter(user=user, token=token_key)
    if not _user_token.exists():
        return None 
    _user = _user_token.first()
    assert user == _user
    _user.attempts += 1
    if _user.attempts >= _user.max_attempt:
        _user.expired = True
        _user.expired_at = timezone.now()
    _user.save()
    return _user