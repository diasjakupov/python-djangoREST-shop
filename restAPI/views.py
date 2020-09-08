from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, HttpResponse
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from .filters import *
from django.contrib.auth import get_user

from .models import Product, Order, Rating, CardProduct, Review
from restAPI.api.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CreateRatingSerializer,
    CardProductSerializer,
    OrderListSerializer,
    AddProductToOrder,
    OrderDetailSerializer,
    ReviewsSerializer,
    CategorySerializer
)

"""Product Views"""


class TestView(APIView):
    def get(self, request):
        print(get_user(request=request))


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PriceFilter
    permission_classes = [permissions.IsAdminUser, ]

    def get_queryset(self):
        qs = Product.objects.all()
        return qs


class ProductCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailView(APIView, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin):

    def get(self, request, pk):
        detail_page = Product.objects.filter().prefetch_related('reviews').get(pk=pk)
        serializer = ProductDetailSerializer(detail_page)
        data = serializer.data
        try:
            rating = Rating.objects.filter(product__id=serializer.data['id'])
            for item in rating:
                if item.user.id == request.user.id:
                    data['is_assessed'] = True
        except:
            data['is_assessed'] = False
        return Response(data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().prefetch_related('subcategory')


class CreateRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer
    queryset = Rating.objects.all()


"""Order Views"""


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class AddProductToOrderView(generics.CreateAPIView):
    queryset = CardProduct.objects.all()
    serializer_class = AddProductToOrder


class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.all().prefetch_related('products').prefetch_related('products__product')


class CardProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardProduct.objects.all()
    serializer_class = CardProductSerializer


"""Reviews"""


class CreateReviewsView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
