from django.urls import path

from books import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='index'),
    path('create-book/', views.BookCreateView.as_view(), name='create-book'),
    path('detail-book/<int:book_id>/', views.BookDetailView.as_view(), name='detail-book'),
]