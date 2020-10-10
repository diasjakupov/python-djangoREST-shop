from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile, Product, CardProduct, Order, ProductImage
from djoser.signals import user_activated

import os


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            customer=instance, username=instance.username, email=instance.email, id=instance.id)
        print('created')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.username = instance.username
        instance.profile.email = instance.email
        instance.profile.save()
        print('updated')


@receiver(post_save, sender=CardProduct)
def order_price_with_changed_cardproduct(sender, instance, created, **kwargs):
    Order.objects.get(is_active='active').get_price()


@receiver(post_delete, sender=CardProduct)
def order_price_with_deleted_cardproduct(sender, instance, **kwargs):
    try:
        Order.objects.get(is_active='active').get_price()
    except:
        print('order was deleted')


@receiver(post_delete, sender=ProductImage)
def delete_images(sender, instance, **kwargs):
    os.remove(f'./media/{instance.image}')
