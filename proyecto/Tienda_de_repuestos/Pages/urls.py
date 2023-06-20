from django.urls import path
from .views import home

app_name = "Pages"

urlpatterns = [
    path('', home, name="Home"),
        ]