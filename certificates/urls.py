from django.urls import path

from . import views

app_name = 'certificates'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
]
