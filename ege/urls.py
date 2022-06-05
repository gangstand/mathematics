from django.urls import path
from .views import EgePageView

urlpatterns = [
    path('', EgePageView.as_view(), name='ege'),
]