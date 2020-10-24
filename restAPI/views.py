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
    queryset = Category.objects.all().prefetch_related('children').prefetch_related(
        'children__children').prefetch_related('children__parent')


class CreateRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer
    queryset = Rating.objects.all()


"""Order Views"""


class ActiveOrderView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer

    def get_object(self, pk):
        obj = Order.objects.filter(
            customer_id=pk).get(is_active='active')
        return obj

    def get(self, request, **kwargs):
        obj = self.get_object(pk=kwargs['pk'])
        serializer = OrderDetailSerializer(obj)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        obj = self.get_object(pk=kwargs['pk'])
        serializer = OrderDetailSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileOrderList(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        qs = Order.objects.filter(customer=pk).filter(
            ~Q(is_active='active'))
        return qs


class AddProductToOrderView(generics.CreateAPIView):
    queryset = CardProduct.objects.all()
    serializer_class = AddProductToOrder
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsCartAllowed,)

    def get_queryset(self):
        return Order.objects.all().prefetch_related(
            'products', 'products__product__images')


class CardProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardProduct.objects.all()
    serializer_class = CardProductSerializer


"""Profile"""


class ProfileDetailView(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(request, *args, **kwargs):
        qs = Profile.objects.prefetch_related(
            "customer", "customer__order").get(pk=kwargs['pk'])
        serializer = UserDetailSerializer(qs)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        qs = Profile.objects.get(pk=kwargs['pk'])
        user = User.objects.get(customer=qs)
        serializer = UserDetailSerializer(qs, data=request.data)
        if serializer.is_valid():
            user.username = request.data['username']
            user.email = request.data['email']
            user.save()
            serializer.save()
            return Response(serializer.data)


"""Reviews"""


class CreateReviewsView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class Test(APIView):
    def get(request, *args, **kwargs):
        qs = Profile.objects.prefetch_related(
            "customer", "customer__order").get(pk=kwargs['pk'])
        serializer = UserDetailSerializer(qs)
        return Response(serializer.data)
