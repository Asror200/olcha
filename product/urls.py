from django.urls import path

from product import views

urlpatterns = [
    path('', views.CategoriesDetailListApiView.as_view(), name='categories-detail-list'),
    path('category/<slug:slug>/', views.CategoryDetailApiView.as_view(), name='category-detail'),
    path('category/<slug:category_slug>/<slug:slug>/', views.GroupDetailListApiView.as_view(),
         name='group-detail'),
    path('product/view/<slug:slug>/', views.ProductDetailApiView.as_view(), name='product-detail'),
    path('add-product/', views.ProductAddView.as_view(), name='add-product'),
]
