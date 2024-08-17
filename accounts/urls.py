from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('ver_perfil/<int:user_id>/', views.ver_perfil, name='ver_perfil'),
     path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
     path('manage_users/', views.manage_users, name='manage_users'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('give_admin/<int:user_id>/', views.give_admin_privileges, name='give_admin'),
   
]
