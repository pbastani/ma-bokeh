from django.db import models


class Curve(models.Model):
    asOf = models.DateTimeField('Observation Date')
    market_data_path = models.CharField(max_length=200)
    processors_path = models.CharField(max_length=200)
    constructors_path = models.CharField(max_length=200)

