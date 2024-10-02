from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
from user.serializers import UserSerializer


# from rest_framework_simplejwt.tokens import BlacklistToken


# Create your views here.

class UserRegisterApiView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        return user


class UserLogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except KeyError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response(f'error": "Something went wrong {e}', status=500)


