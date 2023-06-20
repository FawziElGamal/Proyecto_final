from django.urls import path
from .views import login_user, logout_user, sign_up, my_profile

app_name = 'Users'

urlpatterns = [
    path('signup/', sign_up, name='SignUp'),
    path('login/', login_user, name='LogIn'),
    path('logout/', logout_user, name='LogOut'),
    path('profile/', my_profile, name="EditProfile"),
]