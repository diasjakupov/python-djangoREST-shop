from django.urls import path
from .views import (
    ListAPIView, 
    ProductCreateView, 
    ProductDetailView,
    OrderListView,
    CreateRatingView,
    AddProductToOrderView,
    OrderDetailView,
    CreateReviewsView
) 



urlpatterns = [
    path('products', ListAPIView.as_view(), name='list'),
    path('products/create', ProductCreateView.as_view(), name='create'),
    path("products/<int:pk>", ProductDetailView.as_view(), name='detail'),
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail_page'),
    path('order/add_to_card/<int:pk>', AddProductToOrderView.as_view(), name='add_product'),
    path('rating/', CreateRatingView.as_view(), name='create_rating'),
    path('review/create', CreateReviewsView.as_view(), name='create_review')
]