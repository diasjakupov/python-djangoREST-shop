from rest_framework import serializers
from ..models import Product, Order, Rating, Review, Category, CardProduct

class ProductListSerializer(serializers.ModelSerializer):
    rating=serializers.CharField(source='get_average_rating', read_only=True)
    class Meta:
        model = Product
        fields = ['title',  'available', 'pk', 'rating']



class CommentaryFilter(serializers.ListSerializer):
    def to_representation(self, data):
        data=data.filter(parent=None)
        return super().to_representation(data)

class ChildrenCommentaryField(serializers.Serializer):
    def to_representation(self, value):
        serializer=self.parent.parent.__class__(value, context=self.context)
        print(value)
        print(self.context)
        print(serializer.data)
        return serializer.data


class ReviewsSerializer(serializers.ModelSerializer):
    children=ChildrenCommentaryField(many=True, required=False)
    class Meta:
        list_serializer_class=CommentaryFilter
        model = Review
        fields=['customer', 'product', 'content', 'children', 'parent']
        read_only_fields=['children']



class ProductDetailSerializer(serializers.ModelSerializer):
    rating=serializers.CharField(source='get_average_rating', read_only=True)
    reviews=ReviewsSerializer(many=True, required=False, read_only=True)
    is_assessed=serializers.BooleanField(default=False, required=False, read_only=True)
    class Meta:
        model = Product
        fields=['id','title','description','available','price', 'rating', 'is_assessed', 'reviews']


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields=['user','product', 'star']

    def create(self, validated_data):
        rating, created= Rating.objects.update_or_create(
            product=validated_data.get('product'),
            user=validated_data.get('user'),
            defaults={'star':validated_data.get('star')}
        )
        return rating




class CardProductSerializer(serializers.ModelSerializer):
    product=serializers.SlugRelatedField(read_only=True , slug_field='title')
    description=serializers.CharField(source='product.description')
    
    class Meta:
        model = CardProduct
        fields=('id','product','description','amount', 'total_price')

    def cleared_queryset(self, queryset):
        print(queryset)
        queryset=queryset.select_related('product').prefetch_related('title', 'description')
        return queryset
        


class OrderListSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField(many=False)
    products=serializers.StringRelatedField(many=True)
    class Meta:
        model=Order
        fields="__all__"

class OrderDetailSerializer(serializers.ModelSerializer):
    products=CardProductSerializer(many=True)
    class Meta:
        model = Order
        fields=['status', 'products', 'total_price']
        read_only_fields=['total_price']
        



    def update(self, instance, validated_data):
        instance.status=validated_data['status']
        instance.save()
        return instance



class AddProductToOrder(serializers.ModelSerializer):
    class Meta:
        model = CardProduct
        fields = ['product', 'card']
        read_only_fields=['card']

    def create(self, validated_data):
        user =  self.context['request'].user
        current_order, created=Order.objects.get_or_create(customer=user, defaults={'is_active':"ACTIVE"})
        product, created=CardProduct.objects.get_or_create(product=validated_data['product'], defaults={'customer':user})
        if not current_order.products.filter(pk=product.pk).exists():
            product.card=current_order
            product.save()
            current_order.get_price()
        return product
                
                
        

