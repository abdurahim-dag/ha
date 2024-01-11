from django.urls import path
from socia.api import views

urlpatterns = [
    path(
        "user/register/",
        views.UserRegistrationView.as_view(),
        name="user-registration",
    ),
    path(
        "user/<int:pk>/",
        views.UserViewSet.as_view({"get": "retrieve"}),
        name="user-profile",
    ),
    path(
        "user/login/",
        views.UserLoginView.as_view(),
        name="user-login",
    ),
]
