from django.urls import path
from .views import StudentsPageView

urlpatterns = [
    path('', StudentsPageView.as_view(), name='students'),
]