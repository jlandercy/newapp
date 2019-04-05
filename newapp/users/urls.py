from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
]