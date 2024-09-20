from django.urls import path

from product import views

urlpatterns = [
    path('category', views.CategoryListApiView.as_view(), name='category-list'),
    path('category-detail/<int:pk>/', views.CategoryDetailApiView.as_view(), name='category-detail'),
    path('group-detail/<int:pk>/', views.GroupDetailListApiView.as_view(), name='group-detail'),
    path('product-detail/<int:pk>/', views.ProductDetailApiView.as_view(), name='product-detail'),
]