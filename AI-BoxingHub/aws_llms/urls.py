from django.urls import path
from . import views

urlpatterns = [
    path('my-affirmations/', views.my_affirmations, name='my_affirmations'),
]
