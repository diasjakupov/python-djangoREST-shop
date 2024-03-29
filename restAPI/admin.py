from django.contrib import admin
from .models import Product, Profile, Order, RatingStars, Rating, Review, CardProduct, Category, ProductImage
from .forms import ProductForm
from django.db.models import Avg
from mptt.admin import MPTTModelAdmin


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['pk', 'title', 'available', 'get_average_rating', 'price']
    ordering = ['pk']
    form = ProductForm
    fields = ['title', 'available', 'description',
              'get_average_rating', 'price', 'category']
    readonly_fields = ['get_average_rating']

    def get_average_rating(self, obj):
        value = obj.rating.aggregate(Avg('star'))
        return value['star__avg']

    get_average_rating.short_description = 'Средний рейтинг'


class RatingAdmin(admin.ModelAdmin):
    list_display = ['star', 'user', 'product', 'id']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'published_date']
    fields = ['user', 'product', 'content', 'published_date', 'parent']
    readonly_fields = ['published_date']
    mptt_level_indent = 5


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer']
    fields = ('is_active', 'customer', 'total_price', 'status')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'pk']


class CardProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    fields = ('product', 'customer', 'amount', 'card', 'total_price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(RatingStars)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CardProduct, CardProductAdmin)
admin.site.register(ProductImage)
