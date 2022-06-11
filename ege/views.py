from django.views.generic import ListView

from ege.models import VariantEge, BlockAlgebraEge, BlockGeometriaEge


class EgePageView(ListView):
    model = VariantEge
    template_name = 'ege.html'
    context_object_name = 'VariantEge'

    def get_context_data(self, **kwargs):
        context = super(EgePageView, self).get_context_data(**kwargs)
        context['BlockAlgebraEge'] = BlockAlgebraEge.objects.all()
        context['BlockGeometriaEge'] = BlockGeometriaEge.objects.all()
        return context
