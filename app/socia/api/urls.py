from django.urls import path
from socia.api import views

urlpatterns = [
  path('user/', views.MoviesListApi.as_view()),
  path('user/<uuid:pk>/', views.MoviesDetailApi.as_view())
  #path('movies/<uuid:pk>/', views.MoviesDetailApi.as_view())
  path('user/register', views.MoviesListApi.as_view()),
]