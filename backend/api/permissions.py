from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission

from recipes.models import Recipe


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff


class IsAdminAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        url = request.build_absolute_uri().split('/')
        ending = url[-1] if url[-1] else url[-2]
        pk = url[-2] if url[-1] else url[-3]
        recipe = get_object_or_404(Recipe, id=pk)
        if ending == 'edit':
            return recipe.author == request.user or request.user.is_staff
        else:
            return request.method in SAFE_METHODS or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        url = request.build_absolute_uri().split('/')
        ending = url[-1] if url[-1] else url[-2]
        if ending == 'edit':
            return obj.author == request.user or request.user.is_staff
        else:
            return (request.method in SAFE_METHODS
                    or obj.author == request.user
                    or request.user.is_staff)
