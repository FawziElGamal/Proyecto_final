from django.urls import path
from .views import home, contact

app_name = "Pages"

urlpatterns = [
    path('', home, name="Home"),
    path('sendmessaje/', contact, name="Contact"),
        ]