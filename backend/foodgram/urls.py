from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path
from django.shortcuts import get_object_or_404

from recipes.models import Recipe


def custom_edit(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    if request.user.is_authenticated() and recipe.author == request.user:
        return HttpResponseRedirect(f'/recipes/{pk}/edit/')
    else:
        return HttpResponseRedirect('/recipes/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/<pk>/edit/', custom_edit),
    path('api/', include('api.urls')),
    path('api/', include('users.urls')),
]
