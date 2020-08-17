from rest_framework import serializers
from ..models import Product, Order, Rating

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title',  'amount', 'pk']



class ProductDetailSerializer(serializers.ModelSerializer):
    rating=serializers.CharField(source='get_average_rating', read_only=True)
    class Meta:
        model = Product
        fields=['title','description','amount','price', 'rating']

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields=['user','product', 'star']

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            star=validated_data.get('star'),
            product=validated_data.get('product'),
            user=validated_data.get('user'),
            defaults={'star':validated_data.get('star')}
        )
        return rating


class OrderListSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField(many=False)
    products=serializers.StringRelatedField(many=True)
    class Meta:
        model=Order
        fields="__all__"
