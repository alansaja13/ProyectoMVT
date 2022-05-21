from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Familia

# Create your views here.

def cargarfamilia(request):
    familiar = Familia.objects.all()
    dicc = {'familiar': familiar}
    template = loader.get_template("familia.html")
    documento = template.render(dicc)

    return HttpResponse(documento)


familiar1= Familia(name='Juan', dni=123456789, fecha='20/02/1999')
familiar1.save()
familiar2= Familia(name='Pedro', dni=987654321, fecha='20/04/1994')
familiar2.save()