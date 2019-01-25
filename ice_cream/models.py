from django.db import models
# from models import base_flavor


class IceCream (models.Model):
    base_flavor = (
        ('chocolate', 'Chocolate'),
        ('vanilla', 'Vanilla'),
    )
    available = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('seasonal', 'Seasonal'),
    )
    flavor = models.CharField(max_length=100)
    base = models.CharField(max_length=100, choices=base_flavor, default='Vanilla')
    availability = models.CharField(max_length=100, choices=available, default='Cookies and Creme')
    featured = models.BooleanField()
    date_churned = models.DateField()

    def __str__(self):
        return self.flavor

