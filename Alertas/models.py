import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Medicao(models.Model):
	localizacao = models.CharField(max_length=50)
	data_med = models.DateTimeField('data da med')
	valor = models.DecimalField(max_digits=6, decimal_places = 3)

	def __str__(self):
		return self.localizacao

	def foi_publicado_recentemente(self):
		return self.data_med >= timezone.now() - datetime.timedelta(days=1)