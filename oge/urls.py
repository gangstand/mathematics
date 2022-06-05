from django.urls import path
from .views import OgePageView

urlpatterns = [
    path('', OgePageView.as_view(), name='oge'),
]