from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(customer=instance, username=instance.username, email=instance.email)
        print('created')
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created,**kwargs):
    if created==False:
        instance.profile.username=instance.username
        instance.profile.email=instance.email
        instance.profile.save()
        print('updated')