from books.models import Book
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


# Create your views here.

class BooksListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        data = {}
        for book in Book.objects.all():
            data[book.title] = {"book_id": book.id,
                                "author": book.author,
                                "title": book.title,
                                "published": book.published_date,
                                "description": book.description
                                }

        return Response(data)
