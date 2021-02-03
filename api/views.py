from django.shortcuts import render
from django.views.generics import TemplateView


class AllQoutes(TemplateView):
    template_name = 'api/allquotes.html'
    def get_context_data(self, *args, **kwargs):
        pass