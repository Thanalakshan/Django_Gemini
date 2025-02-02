from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),  # Default route for login
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),  # Ensure this path is present
    path('logout/', views.user_logout, name='logout'),
    path('chat/', views.chat, name='chat'),
]

