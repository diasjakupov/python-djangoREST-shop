from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, HttpResponse
from rest_framework import status

from .models import Product, Order,Rating, CardProduct
from restAPI.api.serializers import (
    ProductListSerializer, 
    ProductDetailSerializer,
    CreateRatingSerializer,
    CardProductSerializer,
    OrderListSerializer,
    AddProductToOrder,
    OrderDetailSerializer)

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
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class ProductDetailView(generics.GenericAPIView ,mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerializer 

    def get(self, request, pk):
        detail_page=get_object_or_404(Product, pk=pk)
        serializer=ProductDetailSerializer(detail_page)
        data=serializer.data
        try:
            rating=Rating.objects.filter(product__id=serializer.data['id'])
            for item in rating:
                if item.user.id==request.user.id:
                    data['is_assessed']=True
        except:

            data['is_assessed']=False
        return Response(data)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CreateRatingView(generics.CreateAPIView):
    serializer_class=CreateRatingSerializer
    queryset=Rating.objects.all()
    




"""Order Views"""

class OrderListView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderListSerializer

class AddProductToOrderView(generics.CreateAPIView):
    queryset=CardProduct.objects.all()
    serializer_class=AddProductToOrder


class OrderDetailView(generics.RetrieveUpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderDetailSerializer



        
        
        

    
   
        



    

    
        

        
        
