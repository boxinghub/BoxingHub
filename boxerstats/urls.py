# boxerstats/urls.py

from django.urls import path, re_path
from .views import BoxerCreateAPIView, BoxerStatsViewSet, dashboard_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'boxer-stats', BoxerStatsViewSet, basename='boxer-stats')

urlpatterns = [
    path('boxers/create/', BoxerCreateAPIView.as_view(), name='boxer-create'),
    path('boxer-stats/', BoxerStatsViewSet.as_view({'get': 'list'}), name='boxer-stats-list'),     # view boxer stats
    path('boxer-stats/<int:pk>/', BoxerStatsViewSet.as_view({'get': 'retrieve'}), name='boxer-stats-detail'),  # view specific boxer stats
    path('dashboard/', dashboard_view, name='dashboard'),
    re_path(r'^dashboard/.+$', dashboard_view),
]

# http://127.0.0.1:8000/api/dashboard/
