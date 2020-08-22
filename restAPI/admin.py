from django.contrib import admin
from .models import Product, Profile, Order, RatingStars, Rating, Review
from .forms import ProductForm
from django.db.models import Avg


class ProductAdmin(admin.ModelAdmin):
    list_display=['pk','title', 'amount', 'get_average_rating']
    ordering=['pk']
    form=ProductForm
    fields=['title', 'amount','description', 'get_average_rating']
    readonly_fields=['get_average_rating']

    def get_average_rating(self, obj):
        value=obj.rating_set.aggregate(Avg('star'))
        return value['star__avg']

    get_average_rating.short_description='Средний рейтинг'


class RatingAdmin(admin.ModelAdmin):
    list_display=['star', 'user', 'product', 'id']

class ReviewAdmin(admin.ModelAdmin):
    list_display=['customer','product', 'published_date', 'parent']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(RatingStars)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Profile)
admin.site.register(Review, ReviewAdmin)
