from django.shortcuts import render
from django.views.generic import TemplateView
from .scripts import get_quotes


class AllQuotes(TemplateView):
    template_name = 'api/allquotes.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'quotes' : get_quotes(),
        }
        return context