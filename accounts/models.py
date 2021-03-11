from django.db import models
from SurfScopeForecast.models import SurfingInfo
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class ForumUser(models.Model):
    user = models.OneToOneField(
        SurfingInfo, on_delete=models.CASCADE, related_name='profile', default=None)
    status = models.CharField(max_length=16, default='', blank=True)
    bio = models.TextField(
        max_length=2000,
        blank=True,
        default=''
    )
    # This returns if we print an instance of ForumUserData

    def __str__(self):
        return self.user.username

    avatar = models.URLField(default='', blank=True)
    status = models.CharField(max_length=16, default='', blank=True)
    name = models.CharField(max_length=32, default='')

# automatically create a token for each new user


@receiver(post_save, sender=SurfingInfo)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# New superuser profile


@receiver(post_save, sender=SurfingInfo)
def create_superuser_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        ForumUser.objects.create(
            user=instance,
            bio='I am the admin and I manage this website',
            avatar='http://res.cloudinary.com/rengorum/image/upload/v1525768360/admin.png',
            name='Administrator',
            status='Administrator'
        )
