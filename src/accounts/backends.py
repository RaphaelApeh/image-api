from django.contrib.auth.backends import BaseBackend

class AuthoricationBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        ...
        