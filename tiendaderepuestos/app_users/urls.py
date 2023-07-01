from django.urls import path
from .views import login_user, logout_user, sign_up, my_profile, pass_change

app_name = 'app_users'

urlpatterns = [
    path('sign-up/', sign_up, name='SignUp'),
    path('log-in/', login_user, name='LogIn'),
    path('log-out/', logout_user, name='LogOut'),
    path('profile/', my_profile, name="EditProfile"),
    path('profile/pass-change', pass_change, name="PassChange"),
]