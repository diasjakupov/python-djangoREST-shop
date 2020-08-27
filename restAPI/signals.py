from django.contrib.auth.models import User

from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from .models import Profile, Product, CardProduct, Order


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(customer=instance, username=instance.username, email=instance.email, id=instance.id)
        print('created')
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created,**kwargs):
    if created==False:
        instance.profile.username=instance.username
        instance.profile.email=instance.email
        instance.profile.save()
        print('updated')




@receiver(post_save, sender=CardProduct)
def set_a_price(sender, created, instance, **kwargs):
    if created==True:
        print('ok')
        try:
            instance.get_total_price()
            instance.save()
        except:
            print('error')
    
    
   

