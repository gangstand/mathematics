from django.views.generic import TemplateView, ListView

from main.models import Cert


class HomePageView(ListView):
    model = Cert
    template_name = 'index.html'
