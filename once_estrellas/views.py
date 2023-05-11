from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Socios_socias, Estacionamiento, Actividades, Alquiler_salones

def Lugar_estacionamiento(request):
    datos = Estacionamiento.objects.all()
    respuesta = "Tu número de estacionamiento es: "
    for dato in datos:
        respuesta += dato.numero_estacionamiento + "<br>"
    return HttpResponse(respuesta)

def listar_socios(request):
    contexto = {
        "socios_as": Socios_socias.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='once_estrellas/lista_socios_socias.html',
        context=contexto,
    )
    return http_response

def Actividades_en_el_club(request):
    datos = Actividades.objects.all()
    respuesta = "Las actividades son: "
    for dato in datos:
        respuesta += dato.nombre + "<br>"
    return HttpResponse(respuesta)

def Salones(request):
    datos = Alquiler_salones.objects.all()
    respuesta = "El salon es: "
    for dato in datos:
        respuesta += dato.tipo_salon + "<br>"
    return HttpResponse(respuesta)

