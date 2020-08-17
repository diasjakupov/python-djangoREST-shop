from django.urls import path
from .views import (
    ListAPIView, 
    ProductCreateView, 
    ProductDetailView,
    OrderListView,
    CreateRatingView
) 



urlpatterns = [
    path('products', ListAPIView.as_view(), name='list'),
    path('products/create', ProductCreateView.as_view(), name='create'),
    path("products/<int:pk>", ProductDetailView.as_view(), name='detail'),
    path('order/', OrderListView.as_view(), name='order_list'),
    path('rating/', CreateRatingView.as_view(), name='create_rating')
]