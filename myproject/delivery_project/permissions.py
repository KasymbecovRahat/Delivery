from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'владелец':
            return True
        return False


class CheckStoreOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CheckStoreOrders(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.product.store.owner

