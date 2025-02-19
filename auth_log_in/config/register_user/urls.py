from django.urls import path, include


app_name = "register_user"
urlpatterns = [
    path("api/auth/", include("rest_registration.api.urls")),
]
