from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    OrderListView,
    CreateRatingView,
    AddProductToOrderView,
    OrderDetailView,
    CreateReviewsView,
    CardProductDetailView,
    CategoryListView,
    TestView
)


urlpatterns = [
    path('', TestView.as_view()),
    path('products', ProductListView.as_view(), name='products_list'),
    path('category', CategoryListView.as_view(), name='categories_list'),
    path('products/create', ProductCreateView.as_view(), name='create'),
    path("products/<int:pk>", ProductDetailView.as_view(), name='detail'),
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail_page'),
    path('detail_card_product/<int:pk>',
         CardProductDetailView.as_view(), name='delete_card_product'),
    path('order/add_to_card/', AddProductToOrderView.as_view(), name='add_product'),
    path('rating/', CreateRatingView.as_view(), name='create_rating'),
    path('review/create', CreateReviewsView.as_view(), name='create_review')
]
