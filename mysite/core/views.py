from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Document


class DocumentCreateView(CreateView):
    model = Document
    template_name = "core/index.html"
    fields = ['upload', ]
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context
