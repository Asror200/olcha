from rest_framework import generics, views
from product import serializers
from rest_framework.response import Response
from product.models import Category, Group, Product
from rest_framework import status
from django.http import Http404


# Create your views here.

class CategoriesDetailListApiView(generics.ListCreateAPIView):
    """ This class displays list of categories,
        you can also add a new category """
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


class Detail(views.APIView):
    def get_object(self, slug):
        try:
            return Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404()

    def get(self, request, slug):
        product = self.get_object(slug)
        serializer = serializers.ProductDetailSerializer(product)
        return Response(serializer.data)

    def delete(self, request, slug):
        product = self.get_object(slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupDetailListApiView(generics.RetrieveUpdateDestroyAPIView):
    """ This class displays detail of a group (products list),
        in this class you can perform various actions on groups """

    serializer_class = serializers.GroupSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        group_slug = self.kwargs.get('slug')
        return Group.objects.prefetch_related('products').filter(
            slug=group_slug
        )

    def get(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(group)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(group, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """ This class displays a detail view of product,
        additionally you can perform various actions on products
        """
    serializer_class = serializers.ProductDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get(self.lookup_field)
        return Product.objects.get(slug=slug)

    def get_object(self):
        queryset = self.get_queryset()
        try:
            return queryset
        except Product.DoesNotExist:
            raise Http404("Not found.")

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAddView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('id')[:1]
    serializer_class = serializers.ProductSerializer
