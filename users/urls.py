from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('settings', views.settings, name='settings'),
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('edit/<str:email>', views.editUser, name='edit'),
    path('delete/<str:email>', views.deleteUser, name='delete'),
]
