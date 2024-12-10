from django.conf import settings
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token


def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_user_token, sender=settings.AUTH_USER_MODEL)