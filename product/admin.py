from django.contrib import admin
from product.models import Product, Category, Group, Attribute, ProductAttributeValue, Value, ProductImage


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


@admin.register(Attribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'attribute']
    search_fields = ['attribute']


@admin.register(Value)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'value']
    search_fields = ['value']


@admin.register(ProductAttributeValue)
class ProductValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'attribute', 'value']
    search_fields = ['product', 'value']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    search_fields = ['product']
