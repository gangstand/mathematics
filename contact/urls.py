from django.urls import path
from .views import ContactCreate, PoliticView

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact'),
    path('politic', PoliticView, name='politic')
]