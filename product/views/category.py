from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from product.models import Category
from product import serializers


class CategoriesDetailListApiView(generics.ListCreateAPIView):
    """ This class displays list of categories,
        you can also add a new category """
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.prefetch_related('groups__products').all()
    serializer_class = serializers.CategoriesGroupsProductsSerializer


class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """ This class displays detail of category,
        in this class you can perform various actions on a category """
    serializer_class = serializers.CategoriesGroupsProductsSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Category.objects.prefetch_related('groups__products').all()

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