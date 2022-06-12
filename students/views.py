from django.views.generic import TemplateView, ListView, DetailView

from students.models import OneCourseVideo, TwoCourseVideo, MetodicalOneCourses, MetodicalTwoCourses


# Страница студенты
class StudentsPageView(TemplateView):
    template_name = 'students.html'

# Видео первого курса
class StudentsOneCourseVideo(ListView):
    model = OneCourseVideo
    template_name = 'video_one_courses.html'

class OneCourseVideoDetail(DetailView):
    model = OneCourseVideo
    template_name = 'vc_detail.html'

# Видео второго курса
class StudentsTwoCourseVideo(ListView):
    model = TwoCourseVideo
    template_name = 'video_two_courses.html'

class TwoCourseVideoDetail(DetailView):
    model = TwoCourseVideo
    template_name = 'vc_detail.html'

# Методические указания
class MetodicalOne(ListView):
    model = MetodicalOneCourses
    template_name = 'Met_instr.html'

class MetodicalTwo(ListView):
    model = MetodicalTwoCourses
    template_name = 'Met_instr.html'
