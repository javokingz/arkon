from django.db import models

# Create your models here.
class Position(models.Model):
    """"Modelo para las unidades y alcaldias"""
    #position_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    geographic_point = models.CharField(max_length=50)
    alcaldia = models.CharField(max_length=50)
    status = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)