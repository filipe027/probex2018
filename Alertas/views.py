from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from fcm_django.fcm import fcm_send_topic_message

from .models import Medicao

import json
from django.core import serializers

# Create your views here.

def index(request):
	return HttpResponse("Ola mundo!")

def upload(request, loc, data, valor_med,senha):
	if(senha=="probex2018"):
		m = Medicao(localizacao=loc, data_med=datetime.strptime(data, '%d_%m_%Y_%H_%M_%S'), valor=valor_med)
		m.save()
		return HttpResponse("Dado salvo no banco de dados com suscesso.")
	else:
		return HttpResponse("Senha Errada")

def upload_server_date(request, loc, valor_med,senha):
	if(senha=="probex2018"):
		m = Medicao(localizacao=loc, data_med=datetime.now(), valor=valor_med)
		m.save()
		fcm_send_topic_message(topic_name='news', message_body='Nivel de chuva de %d mm no local: %s' %(valor_med, loc), message_title='Alerta em: %s' % loc)

		return HttpResponse("Dado salvo no banco de dados com suscesso.")
	else:
		return HttpResponse("Senha Errada")

def latest_med(request, n_med):
	data = serializers.serialize('json', Medicao.objects.all().order_by('-id')[:n_med], fields=('localizacao', 'data_med', 'valor'))
	data = json.loads(data)
	data_f = []
	for i in range(0, len(data)):
		data_f.append(data[i]['fields'])
	data_f = json.dumps(data_f)
	return HttpResponse(data_f, content_type='application/json')

def home(request):
	
	return HttpResponse("Bem vindo ao site do Probex Chuvas 2018")
