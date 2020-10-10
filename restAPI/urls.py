from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ActiveOrderView,
    CreateRatingView,
    AddProductToOrderView,
    OrderDetailView,
    CreateReviewsView,
    CardProductDetailView,
    CategoryListView,
    ProfileDetailView,
    ProfileOrderList
)


urlpatterns = [
    path('products', ProductListView.as_view(), name='products_list'),
    path('category', CategoryListView.as_view(), name='categories_list'),
    path("products/<int:pk>", ProductDetailView.as_view(), name='detail'),
    path('profile/active_order',
         ActiveOrderView.as_view(), name='order_list'),
    path('profile/orders/<int:pk>/', ProfileOrderList.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail_page'),
    path('detail_card_product/<int:pk>',
         CardProductDetailView.as_view(), name='delete_card_product'),
    path('order/add_to_card/', AddProductToOrderView.as_view(), name='add_product'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(),
         name='detail_page_of_profile'),
    path('rating/', CreateRatingView.as_view(), name='create_rating'),
    path('review/create', CreateReviewsView.as_view(), name='create_review')
]
