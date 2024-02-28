from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register , name="register"),
    path('mylogin',views.my_login, name="mylogin"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('profile-management',views.profile_management, name="profile-management"),
]