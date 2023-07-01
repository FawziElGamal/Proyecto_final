from django.urls import path
from .views import home, contact

app_name = "pages"

urlpatterns = [
    path('', home, name="Home"),
    path('send-messaje/', contact, name="Contact"),
        ]