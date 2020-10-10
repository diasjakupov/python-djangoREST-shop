from rest_framework import permissions


class IsCartAllowed(permissions.BasePermission):
    message = 'Page Not Found'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer
