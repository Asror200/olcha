from books.models import Book
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from books.serializers import BookSerializer


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


class BookDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, book_id, format=None):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class BookCreateView(APIView):
    def get(self, request):
        data = {}
        for book in Book.objects.all():
            data[book.title] = {"book_id": book.id,
                                "author": book.author,
                                "title": book.title,
                                "published": book.published_date,
                                "description": book.description
                                }

        return Response(data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
