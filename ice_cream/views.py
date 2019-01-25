from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

class HomeView(TemplateView):
    template_name = 'ice_cream/home.html'

    def get_context_data(self, **kwargs):
        chocolate_ice_cream = models.IceCream.objects.filter(base='Chocolate')

        context = {
            'chocolate_base': chocolate_ice_cream
        }
        return context
