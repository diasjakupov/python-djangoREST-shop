from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, F, Sum


class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=300, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=300)
    tags = models.ForeignKey(
        'self', null=True, on_delete=models.CASCADE, blank=True, related_name='subcategory')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductQuerySet(models.QuerySet):
    pass


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    description = models.TextField(null=True)
    available = models.IntegerField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    objects = ProductManager()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_average_rating(self):
        value = self.rating_set.aggregate(Avg(F('star')))['star__avg']
        return value

    def __str__(self):
        return f'{self.title}, id:{self.pk}'


def foldername(instance, filename):
    return f'{instance.product.title}/{filename}'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=foldername)


class Order(models.Model):
    STATUS = [('deliver', 'deliver'), ('pickup', 'pickup')]
    ACTIVE_STATUS = [('active', 'active'), ('completed',
                                            'completed'), ('preparation', 'preparation')]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=200, choices=STATUS, default='deliver')
    total_price = models.FloatField(null=True, default=0)
    is_active = models.CharField(
        default='active', null=True, choices=ACTIVE_STATUS, max_length=75)

    def get_price(self):
        self.total_price = self.products.aggregate(
            Sum('total_price'))['total_price__sum']
        self.save()
        return self.total_price

    def __str__(self):
        idx = str(self.id)
        return idx


class CardProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, unique=False)
    amount = models.IntegerField(default=1, null=True, unique=False)
    total_price = models.FloatField(
        default=0, unique=False, null=True, max_length=4)
    card = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, related_name='products')

    def get_total_price(self):
        product_price = self.product.price
        self.total_price = product_price*float(self.amount)
        self.total_price = round(self.total_price)
        return self.total_price

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        self.get_total_price()
        return super(CardProduct, self).save(*args, **kwargs)


class RatingStars(models.Model):
    value = models.IntegerField(null=True)

    def __str__(self):
        value = str(self.value)
        return value


class Rating(models.Model):
    star = models.ForeignKey(RatingStars, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        star = str(self.star)
        return star


class Review(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Покупатель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, verbose_name="Товар", related_name='reviews')
    content = models.TextField(null=True)
    published_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации")
    changed_date = models.DateTimeField(auto_now=True, null=True)
    parent = models.ForeignKey('self', null=True, default=None,
                               on_delete=models.CASCADE, blank=True, related_name='children')

    def __str__(self):
        return f'{self.customer.username} : {self.content}'
