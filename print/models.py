from django.db import models

# Create your models here.
class Amiibo(models.Model):
    amiiboSeries = models.CharField(max_length=50)
    character = models.CharField(max_length=50)
    gameSeries = models.CharField(max_length=50)
    head = models.CharField(max_length=50)
    image = models.CharField(max_length=256)
    name = models.CharField(max_length=50)
    tail = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name