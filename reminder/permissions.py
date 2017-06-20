from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class UserPermissionsAll(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

class UserPermissionsObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class UserNoPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated():
            return False
        else:
            return True
