from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Teste para aplicativo chuvas ufpb!")

def easter_egg(request):
    return HttpResponse("Ficou interessada né safada hmmm")
