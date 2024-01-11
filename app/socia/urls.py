from django.urls import include, path

urlpatterns = [
    path("", include("socia.api.urls")),
]
