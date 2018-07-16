from django.db import models

# Create your models here.

class Medicao(models.Model):
	localizacao = models.CharField(max_length=50)
	data_med = models.DateTimeField('data da med')
	valor = models.DecimalField(max_digits=6, decimal_places = 3)