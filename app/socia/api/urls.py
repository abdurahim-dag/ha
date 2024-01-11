from django.urls import path
from socia.api import views

urlpatterns = [
    #   path('user/', views.MoviesListApi.as_view()),
    #   #path('movies/<uuid:pk>/', views.MoviesDetailApi.as_view())
    #   path('user/register', views.MoviesListApi.as_view()),
    path(
        "user/register/",
        views.UserRegistrationView.as_view(),
        name="user-registration",
    ),
    path(
        "user/<int:id>/",
        views.UserViewSet.as_view({"get": "retrieve"}),
        name="user-profile",
    ),
    path(
        "user/login/",
        views.UserLoginView.as_view(),
        name="user-login",
    ),
]
