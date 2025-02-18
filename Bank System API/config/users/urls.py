from django.urls import include, path
from .views import RegisterUserview

app_name = "users"


urlpatterns = [
    path('register/', RegisterUserview, name='register'),
]