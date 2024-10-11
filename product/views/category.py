from django.views.decorators.cache import cache_page
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from product.models import Category
from product import serializers
from product.permissions import IsOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.core.cache import cache


class CategoriesDetailListApiView(generics.ListCreateAPIView):
    """ This class displays list of categories,
        you can also add a new category """
    permission_classes = [AllowAny]
    cache_key = 'category-list'
    queryset = Category.objects.prefetch_related(
        'groups',
        'groups__products__comments',
        'groups__products__images',
        'groups__products__users_like'
    )
    serializer_class = serializers.CategoriesGroupsProductsSerializer

    def get(self, request, *args, **kwargs):
        cached_data = cache.get(self.cache_key)
        if cached_data:
            return Response(cached_data)

        response = super().get(request, *args, **kwargs)
        cache.set(self.cache_key, response.data, timeout=60)
        return response


@method_decorator(cache_page(60), name='dispatch')
class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """ This class displays detail of category,
        in this class you can perform various actions on a category """
    permission_classes = [AllowAny]
    serializer_class = serializers.CategoriesGroupsProductsSerializer
    lookup_field = 'slug'
    cache_key = 'category-detail'

    def get_queryset(self):
        queryset = Category.objects.prefetch_related(
            'groups',
            'groups__products__comments',
            'groups__products__users_like',
        ).all()
        return queryset

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryAddView(generics.CreateAPIView):
    serializer_class = serializers.CategoriesGroupsProductsSerializer
