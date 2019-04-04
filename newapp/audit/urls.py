from django.urls import path

from . import views

app_name = 'audit'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sessions/', views.SessionsView.as_view(), name='sessions'),
    path('sessions/<int:pk>/', views.SessionsView.as_view(), name='sessions'),
]