from rest_framework.views import APIView
from product.serializers import CategorySerializer, GroupSerializer, ProductSerializer
from rest_framework.response import Response
from product.models import Category, Group, Product
from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.


class CategoryListApiView(APIView):
    """ This class displays list of categories,
        you can also add a new category"""
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CategoryDetailApiView(APIView):
    """ This class displays detail of category (list of groups),
        in this class you can perform various actions on a category
        and add a new group"""
    def get(self, request, pk):
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        category.delete()


class GroupDetailListApiView(APIView):
    """ This class displays detail of group (products list),
        in this class you can perform various actions on groups
        and add a new product """
    def get(self, request, pk):
        queryset = Product.objects.filter(group_id=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = GroupSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = GroupSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        group = get_object_or_404(Group, pk=pk)

        group.delete()


class ProductDetailApiView(APIView):
    """ This class displays the detail view of a product.
        additionally you can perform various actions on products"""
    def get(self, request, pk):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        if product:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
