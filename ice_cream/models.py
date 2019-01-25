from django.db import models
# from models import base_flavor


class IceCream (models.Model):
    CHOCOLATE = 'Chocolate'
    VANILLA = 'Vanilla'

    base_flavor = (
        (CHOCOLATE, 'Chocolate'),
        (VANILLA, 'Vanilla'),
    )
    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    SEASONAL = 'Seasonal'
    available = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (SEASONAL, 'Seasonal'),
    )
    flavor = models.CharField(max_length=100)
    base = models.CharField(max_length=100, choices=base_flavor, default='Vanilla')
    availability = models.CharField(max_length=100, choices=available, default='Cookies and Creme')
    featured = models.BooleanField()
    date_churned = models.DateField()

    def __str__(self):
        return self.flavor

