from django.urls import path
from . import views # From Prospect
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.Prospect_List.get_all, name='wishlist'),
    path('register_beta/', views.Prospect_List.register_beta, name='register_beta'),
    path('activate/<activation_token>/', views.Prospect_List.activate, name='activate'),
]
