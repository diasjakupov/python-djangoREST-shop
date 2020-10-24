from rest_framework import permissions
from .models import Order


class IsCartAllowed(permissions.BasePermission):
    message = 'You cant do this'

    def has_permission(self, request, view):
        order = Order.objects.prefetch_related('customer').get(
            pk=request.parser_context['kwargs']['pk'])
        return bool(request.user.id == order.customer.id)
