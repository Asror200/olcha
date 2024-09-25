from django.contrib import admin
from product.models import (
    Product, Category, Group,
    AttributeKey, ProductAttributeValue,
    ProductImage, Comment, AttributeValue)


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category_id', 'image']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'category_id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'discount', 'quantity', 'group_id']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'group_id']
    autocomplete_fields = ('users_like',)


@admin.register(AttributeKey)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'key']
    search_fields = ['key']


@admin.register(AttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'value']
    search_fields = ['value']


@admin.register(ProductAttributeValue)
class ProductValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'key', 'value']
    search_fields = ['product', 'value']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    search_fields = ['product']


@admin.register(Comment)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'product', 'user', 'image', 'text']
    search_fields = ['product']
