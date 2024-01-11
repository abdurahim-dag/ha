from django.urls import path, include


urlpatterns = [
    path("api/", include("socia.api.urls")),
]

handler500 = "rest_framework.exceptions.server_error"
handler400 = "rest_framework.exceptions.bad_request"
