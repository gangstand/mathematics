from django.urls import path
from .views import PollsListView, PoolsDetailView

urlpatterns = [
    path('', PollsListView.as_view(), name='polls'),
    path('<uuid:pk>', PoolsDetailView.as_view(), name='book_detail'),
]