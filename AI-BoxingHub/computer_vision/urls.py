from django.urls import path
from . import views

urlpatterns = [
    path('', views.computer_vision, name='computer_vision'),
]
