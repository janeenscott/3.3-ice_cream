from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from .models import IceCream

class HomeView(TemplateView):
    template_name = 'ice_cream/home.html'

    def get_context_data(self, **kwargs):
        featured_flavors = IceCream.objects.filter(featured=True)
        daily_flavors = IceCream.objects.filter(availability='daily')
        weekly_flavors = IceCream.objects.filter(availability='weekly')
        seasonal_flavors = IceCream.objects.filter(availability='seasonal')

        context = {
            'featured': featured_flavors,
            'daily': daily_flavors,
            'weekly': weekly_flavors,
            'seasonal': seasonal_flavors
        }

        return context
