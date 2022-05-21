from django.urls import path
from familia_app import views

urlpatterns = [
    path('datos/', views.cargarfamilia),
    ]