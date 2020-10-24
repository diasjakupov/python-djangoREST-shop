from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Profile, Product, CardProduct, Order, ProductImage
from djoser.signals import user_activated
from django.db.models import F

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
        instance.customer.username = instance.username
        instance.customer.email = instance.email
        instance.customer.save()
        print('updated')


@receiver(post_save, sender=CardProduct)
def order_price_with_changed_cardproduct(sender, instance, created, **kwargs):
    if created==False:
        order=Order.objects.get(pk=instance.card.id)
        if order.is_active!='active':
            raise Exception('the cart you chose is not available')
        else:
            order.get_price()
        return True

@receiver(post_delete, sender=CardProduct)
def order_price_with_deleted_cardproduct(sender, instance, **kwargs):
    Order.objects.get(pk=instance.card.id).get_price()



@receiver(post_delete, sender=ProductImage)
def delete_images(sender, instance, **kwargs):
    os.remove(f'./media/{instance.image}')
