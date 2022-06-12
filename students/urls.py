from django.urls import path
from .views import StudentsPageView, StudentsOneCourseVideo, OneCourseVideoDetail, StudentsTwoCourseVideo, \
    TwoCourseVideoDetail, MetodicalOne, MetodicalTwo

urlpatterns = [
    path('', StudentsPageView.as_view(), name='students'),
    path('ocv/', StudentsOneCourseVideo.as_view(), name='ocv'),
    path('ocv/<int:pk>/', OneCourseVideoDetail.as_view(), name='ocv_detail'),
    path('otv/', StudentsTwoCourseVideo.as_view(), name='otv'),
    path('otv/<int:pk>/', TwoCourseVideoDetail.as_view(), name='otv_detail'),
    path('metone/', MetodicalOne.as_view(), name='metodical_one'),
    path('mettwo/', MetodicalTwo.as_view(), name='metodical_two'),
]