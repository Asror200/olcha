from rest_framework import generics, status, permissions
from rest_framework.response import Response
from product import serializers
from product.models import Product, AttributeKey, AttributeValue, ProductAttributeValue
from django.http import Http404

from product.permissions import IsOwnerOrReadOnly


class ProductsListApiView(generics.ListCreateAPIView):
    """ This class used to display all products, and you can add a new product """
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """ This class is used to display a detail view of product,
        additionally you can perform various actions on products
        """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = serializers.ProductDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get(self.lookup_field)
        return Product.objects.get(slug=slug)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

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


class ProductAddView(generics.CreateAPIView):
    """ This class is used to add a new product to the database """
    serializer_class = serializers.ProductSerializer


class AttributeKeyListApiView(generics.ListCreateAPIView):
    queryset = AttributeKey.objects.all()
    serializer_class = serializers.AttributeKeySerializer


class AttributeValueListApiView(generics.ListCreateAPIView):
    queryset = AttributeValue.objects.all()
    serializer_class = serializers.AttributeValueSerializer


class AttributeKeyValueListApiView(generics.ListCreateAPIView):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = serializers.AttributeKeyValueSerializer
