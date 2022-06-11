from django.views.generic import ListView

from oge.models import VariantOge, BlockAlgebraOge, BlockGeometriaOge


class OgePageView(ListView):
    model = VariantOge
    template_name = 'oge.html'
    context_object_name = 'VariantOge'

    def get_context_data(self, **kwargs):
        context = super(OgePageView, self).get_context_data(**kwargs)
        context['BlockAlgebraOge'] = BlockAlgebraOge.objects.all()
        context['BlockGeometriaOge'] = BlockGeometriaOge.objects.all()
        return context
