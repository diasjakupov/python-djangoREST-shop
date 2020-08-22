from rest_framework import serializers
from ..models import Product, Order, Rating, Review

class ProductListSerializer(serializers.ModelSerializer):
    rating=serializers.CharField(source='get_average_rating', read_only=True)
    class Meta:
        model = Product
        fields = ['title',  'amount', 'pk', 'rating']



class CommentaryFilter(serializers.ListSerializer):
    def to_representation(self, data):
        data=data.filter(parent=None)
        return super().to_representation(data)

class ChildrenCommentaryField(serializers.Serializer):
    def to_representation(self, value):
        serializer=self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewsSerializer(serializers.ModelSerializer):
    children=ChildrenCommentaryField(many=True)
    class Meta:
        list_serializer_class=CommentaryFilter
        model = Review
        fields=['customer', 'product', 'content', 'children']



class ProductDetailSerializer(serializers.ModelSerializer):
    rating=serializers.CharField(source='get_average_rating', read_only=True)
    reviews=ReviewsSerializer(many=True, required=False, read_only=True)
    is_assessed=serializers.BooleanField(default=False, required=False, read_only=True)
    class Meta:
        model = Product
        fields=['id','title','description','amount','price', 'rating', 'is_assessed', 'reviews']

    




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


class OrderListSerializer(serializers.ModelSerializer):
    customer=serializers.StringRelatedField(many=False)
    products=serializers.StringRelatedField(many=True)
    class Meta:
        model=Order
        fields="__all__"
