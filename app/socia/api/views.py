"""Views."""
from http import HTTPStatus

from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.response import Response

from socia.models import CustomUser
from socia.serializers import UserSignupSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"sign up": "success"}, status=status.HTTP_201_CREATED)


class UserViewSet(
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserLoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"sign in": "success"})

        return Response({"sign in": "exception"}, status=HTTPStatus.UNAUTHORIZED)
