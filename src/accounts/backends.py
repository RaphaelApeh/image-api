from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try:
            user = User.objects.get(email__iexact=username)
            vaildate_user = all([user.check_password(password), user.is_active])
            if vaildate_user:
        
                return user
            else:
                return None 
        except User.DoesNotExist:
            return None
        