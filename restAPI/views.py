from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product, Order,Rating
from restAPI.api.serializers import (
    ProductListSerializer, 
    ProductDetailSerializer,
    OrderListSerializer,
    CreateRatingSerializer)

"""Product Views"""

class ListAPIView(generics.ListAPIView):
    serializer_class=ProductListSerializer
    def get_queryset(self):
        request=self.request
        qs=Product.objects.all()
        filter = request.GET.get('filter')
        if filter is not None:
            qs=qs.filter(title__icontains=filter)
            return qs
        return qs    
    
class ProductCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class ProductDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class=ProductDetailSerializer
    queryset=Product.objects.all()

    def get(self, request, *args, **kwargs):
        data=self.retrieve(request, *args, **kwargs)
        return data

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class CreateRatingView(APIView):
    def post(self, request):
        serializer=CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)




"""Order Views"""

class OrderListView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderListSerializer
