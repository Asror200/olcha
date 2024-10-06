from django.urls import path

from post.views import PostAPIView, PostDetailAPIView

urlpatterns = [
    path('', PostAPIView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
]
