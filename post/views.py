from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models import Post
from post.serializers import PostSerializer
from product.permissions import IsOwnerOrReadOnly


# Create your views here.


class PostAPIView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request):
        posts = Post.objects.select_related('user').all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    queryset = Post.objects.select_related('user').all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
