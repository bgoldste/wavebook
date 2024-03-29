from django.shortcuts import render
from django.views.generic.base import TemplateView


class SpotView(TemplateView):

    template_name = "trestles.html"

    def get_context_data(self, **kwargs):
        context = super(SpotView, self).get_context_data(**kwargs)
        return context

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context