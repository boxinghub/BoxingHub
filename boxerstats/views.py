from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Boxer
from .serializers import BoxerSerializer
from django.views.generic import TemplateView


class BoxerCreateAPIView(generics.ListCreateAPIView):
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer
    
    
class BoxerStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides `list` and `retrieve` for boxer stats"""
    queryset = Boxer.objects.all()
    serializer_class = BoxerSerializer
    
def dashboard_view(request):
    return render(request, "dashboard/index.html")
