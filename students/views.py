from django.views.generic import TemplateView


class StudentsPageView(TemplateView):
    template_name = 'students.html'
