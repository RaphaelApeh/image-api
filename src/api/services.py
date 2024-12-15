import time
import typing
import datetime

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
    try:
        _user  = UserToken.objects.get(user=user, token=token_key)
        time.sleep(1.2)
        _user.attempts += 1
        if _user.attempts >= _user.max_attempt:
            _user.expired_at = datetime.datetime.now()
            _user.expired = True
        _user.save()
        return _user
    except UserToken.DoesNotExist:

        _user = UserToken.objects.create(user=user, token=token_key)
        _user.created_at = datetime.datetime.now()
    
        _user.save()

        return _user