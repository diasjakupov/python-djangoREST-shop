from .models import *
from django.db.models import F

"""Создание декоратора"""


def CheckingAvailableProduct(func):
    def doubleInner(*args, **kwagrs):
        result, product, value = func(*args, **kwagrs)
        product_instanse = Product.objects.get(id=product)
        if result == 1:
            return value
        if product_instanse.available >= result:
            Product.objects.filter(id=product).update(
                available=F('available') - result)
            return value
        else:
            raise ValueError('Продукт больше недоступен')
    return doubleInner


@CheckingAvailableProduct
def AddingCardProduct(value):
    """Провка наличия при первом добавлении товара"""
    product = list(value.items())[0][1]
    return 1, product.id, value


@CheckingAvailableProduct
def UpdatingCardProduct(value, instance):
    """Проверка доступности при обновление CardProduct"""
    amount = list(value.items())[0][1]
    product_id = instance['product_id']
    return amount, product_id, value
