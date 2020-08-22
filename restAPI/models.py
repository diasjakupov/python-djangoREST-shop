from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg



class Profile(models.Model):
    customer=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=300, null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.username




class ProductQuerySet(models.QuerySet):
    pass

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

class Product(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True)
    amount=models.IntegerField(null=True, default=0)
    price=models.FloatField(null=True, default=0)
    objects=ProductManager()
    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'

    def get_average_rating(self):
        value=self.rating_set.aggregate(Avg('star'))
        return value


    def __str__(self):
        return f'{self.title}, id:{self.pk}'




class Order(models.Model):
    products=models.ManyToManyField(Product)
    customer=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    total_price=models.IntegerField(null=True, default=0)




class RatingStars(models.Model):
    value=models.IntegerField(null=True)

    def __str__(self):
        value=str(self.value)
        return value


class Rating(models.Model):
    star=models.ForeignKey(RatingStars, on_delete=models.CASCADE, default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        star=str(self.star)
        return star

class Review(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name="Товар", related_name='reviews')
    content=models.TextField(null=True)
    published_date=models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    changed_date=models.DateTimeField(auto_now=True, null=True)
    parent=models.ForeignKey('self', null=True, default=None, on_delete=models.CASCADE, blank=True, related_name='children')

    def __str__(self):
        return f'{self.customer.username} : {self.content}'




   





    




