from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, HttpResponse
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


from .filters import *
from django.contrib.auth import get_user

from django.db.models import Q, Prefetch

from .models import Product, Order, Rating, CardProduct, Review
from .permissions import IsCartAllowed
from restAPI.api.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CreateRatingSerializer,
    CardProductSerializer,
    AddProductToOrder,
    OrderDetailSerializer,
    ReviewsSerializer,
    CategorySerializer,
    UserDetailSerializer,
    OrderListSerializer
)

"""Product Views"""


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PriceFilter

    def get_queryset(self):
        qs = Product.objects.all().prefetch_related('images')
        return qs


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        products = Product.objects.all().prefetch_related(
            'rating__user', 'reviews__children', 'reviews__user', )
        return products


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().prefetch_related(
        'children').prefetch_related('children__children').prefetch_related('children__parent')


class CreateRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer
    queryset = Rating.objects.all()


"""Order Views"""


class ActiveOrderView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = OrderDetailSerializer

    def get(self, request):
        user = self.request.user
        obj = Order.objects.filter(customer=user).get(is_active='active')
        serializer = OrderDetailSerializer(obj)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProfileOrderList(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        qs = Order.objects.filter(customer=pk).filter(~Q(is_active='active'))
        return qs


class AddProductToOrderView(generics.CreateAPIView):
    queryset = CardProduct.objects.all()
    serializer_class = AddProductToOrder


class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsCartAllowed,)

    def get_queryset(self):
        return Order.objects.all().prefetch_related('products').prefetch_related('products__product')


class CardProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardProduct.objects.all()
    serializer_class = CardProductSerializer


"""Profile"""


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = Profile.objects.prefetch_related(
            'customer__order')
        return qs


"""Reviews"""


class CreateReviewsView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
