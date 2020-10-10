from rest_framework import serializers


from djoser.serializers import UserCreateSerializer
from ..models import Product, Order, Rating, Review, Category, CardProduct, ProductImage, Profile
from django.contrib.auth import get_user, get_user_model
from django.db.models import Q, Prefetch


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']


"""Product and relevant serializer"""


class RecursiveFilter(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ChildrenField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value)
        return serializer.data


class ReviewsSerializer(serializers.ModelSerializer):
    children = ChildrenField(
        many=True)
    user = serializers.StringRelatedField()

    class Meta:
        list_serializer_class = RecursiveFilter
        model = Review
        fields = ['id', 'user', 'content',
                  'parent', 'children', 'published_date']
        read_only_fields = ['children']


class CategorySerializer(serializers.ModelSerializer):
    children = ChildrenField(many=True)

    class Meta:
        model = Category
        fields = ['title', 'children', 'parent_id']
        list_serializer_class = RecursiveFilter


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

    # def get_reviews(self, obj):
    #     data = Review.objects.filter(product=obj).select_related(
    #         'user', 'parent').prefetch_related(Prefetch('children', queryset=Review.objects.all()))
    #     serializer = ReviewsSerializer(data, many=True)
    #     return serializer.data

    def get_is_assessed(self, obj):
        request = self.context['request']
        try:
            users_id = [i.user.id for i in obj.rating.all()]
            if request.user.id in users_id:
                return True
        except:
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
    description = serializers.CharField(source='product.description')

    class Meta:
        model = CardProduct
        fields = ('id', 'product', 'description', 'amount', 'total_price')

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
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ['status', 'id', 'total_price', 'is_active', 'products']


class AddProductToOrder(serializers.ModelSerializer):
    class Meta:
        model = CardProduct
        fields = ['product', 'card']
        read_only_fields = ['card']

    def create(self, validated_data):
        print(validated_data)
        user = self.context['request'].user
        current_order, created = Order.objects.get_or_create(
            is_active="active", defaults={'customer': "user"})
        product, created = CardProduct.objects.get_or_create(
            product=validated_data['product'], defaults={'customer': user})
        if not current_order.products.filter(pk=product.pk).exists():
            product.card = current_order
            product.save()
            current_order.get_price()
        return product


class UserDetailSerializer(serializers.ModelSerializer):
    orders_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['email', 'username', 'phone', 'orders_quantity']

    def get_orders_quantity(self, obj):
        data = obj.customer.order.all()
        return data.count()
