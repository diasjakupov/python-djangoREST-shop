from rest_framework import serializers


from djoser.serializers import UserCreateSerializer
from ..models import Product, Order, Rating, Review, Category, CardProduct, ProductImage, Profile
from django.contrib.auth import get_user, get_user_model
from django.db.models import Q, Prefetch
from ..utils import checkingOrder
from django.db.models import F
from ..validators import AddingCardProduct, UpdatingCardProduct


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']


"""Product and relevant serializer"""


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'content',
                  'parent', 'children', 'published_date']
        read_only_fields = ['children']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'children', 'parent_id']


class ImageSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductListSerializer(serializers.ModelSerializer):
    rating = serializers.CharField(source='get_average_rating', read_only=True)
    category = serializers.StringRelatedField(many=True)
    images = ImageSerizalizer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'price', 'available',
                  'pk', 'rating', 'category', 'images']


class ProductDetailSerializer(serializers.ModelSerializer):
    rating = serializers.CharField(source='get_average_rating', read_only=True)
    reviews = ReviewsSerializer(many=True)
    is_assessed = serializers.SerializerMethodField()
    images = ImageSerizalizer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'available',
                  'price', 'rating', 'is_assessed', 'reviews', 'images']

    def get_is_assessed(self, obj):
        request = self.context['request']
        try:
            users_id = [i.user.id for i in obj.rating.all()]
            if request.user.id in users_id:
                return True
        except BaseException:
            return False


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'product', 'star']

    def create(self, validated_data):
        rating, created = Rating.objects.update_or_create(
            product=validated_data.get('product'),
            user=validated_data.get('user'),
            defaults={'star': validated_data.get('star')}
        )
        return rating


"""Order and etc"""


class CardProductSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='title')
    images = ImageSerizalizer(
        many=True, source='product.images', read_only=True)

    class Meta:
        model = CardProduct
        fields = ('id', 'product', 'product_id',
                  'amount', 'total_price', 'images')
        read_only_fields = ('id',
                            'total_price', 'images')

    def validate(self, data):
        data = UpdatingCardProduct(data, self.initial_data)
        return data

    def update(self, instance, data):
        instance.amount = data['amount']
        instance.save()
        return instance


class OrderDetailSerializer(serializers.ModelSerializer):
    products = CardProductSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'status', 'products', 'total_price', 'is_active']
        read_only_fields = ['total_price']

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance


class OrderListSerializer(serializers.ModelSerializer):
    products = serializers.IntegerField(source='products.count')

    class Meta:
        model = Order
        fields = ['status', 'id', 'total_price',
                  'is_active', 'products']


class AddProductToOrder(serializers.ModelSerializer):
    class Meta:
        model = CardProduct
        fields = ['product']
        validators = [AddingCardProduct]

    def create(self, validated_data):
        """Получаю данные"""
        user = self.context['request'].user
        product_instance = validated_data['product']
        """Проверию существование"""
        """Если нет то создаю и обновляю"""
        try:
            current_order = Order.objects.get(
                customer=user, is_active="active")
        except BaseException:
            current_order = Order.objects.create(
                customer=user, is_active='active', status='deliver')

        product, created = CardProduct.objects.get_or_create(
            product=validated_data['product'], defaults={
                'customer': user, 'product': validated_data['product']})
        if not current_order.products.filter(pk=product.pk).exists():
            product.card = current_order
            product.save()
            current_order.get_price()
            return product
        else:
            """Если существует увеличиваю количество"""
            for cardproduct in current_order.products.all():
                if cardproduct.product == product_instance:
                    CardProduct.objects.filter(
                        product=product_instance,
                        customer=user,
                        card=current_order.id).update(
                        amount=F('amount') + 1)
                    CardProduct.objects.get(
                        product=product_instance,
                        customer=user,
                        card=current_order.id).save()
                    return product


class UserDetailSerializer(serializers.ModelSerializer):
    orders_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'email', 'username', 'phone', 'orders_quantity']

    def get_orders_quantity(self, obj):
        data = obj.customer.order.filter(~Q(is_active='active'))
        return data.count()
