from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token


User = get_user_model()


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    attempts = models.IntegerField(default=0)
    max_attempt = models.IntegerField(default=10)
    created_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return 'token: %s user: %d ' % (self.token, self.user.get_full_name() or self.user.username)
    

    def save(self, **kwargs):
        super().save(**kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['token'], name='validate_token')
        ]


def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_token, sender=settings.AUTH_USER_MODEL)


def create_user_token(instance, created, **kwargs):
    if created:
        UserToken.objects.create(user=instance)
    
post_save.connect(create_user_token, sender=settings.AUTH_USER_MODEL)