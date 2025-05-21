from django.urls import path
from . import views
from .utils import update_like, update_love


urlpatterns = [
    path('', views.index, name='index'),
    path('clubs/', views.clubs, name='clubs'),
    path('fundamentals/', views.fundamentals, name='fundamentals'),
    path('gears/', views.gears, name='gears'),
    path('moments/', views.moments, name='moments'),
    path('recovery/', views.recovery, name='recovery'),
    path('rules/', views.rules, name='rules'),
    path('update_like/', update_like, name='update_like'),
    path('update_love/', update_love, name='update_love'),
    # path('accessibility/', views.accessibility, name='accessibility'),
]   
