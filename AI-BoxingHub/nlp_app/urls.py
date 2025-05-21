from django.urls import path
from . import views

urlpatterns = [
    path('nlp_app/', views.transcribe_and_diarize, name='nlp_app'),
]
