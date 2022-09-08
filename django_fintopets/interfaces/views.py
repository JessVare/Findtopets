from django.shortcuts import render

def inicio(request):
    return render(request, 'interfaces_de_inicio/Inicio.html')

def acercade(request):
    return render(request, 'interfaces_de_inicio/acercade.html')

def masDesaparecidas(request):
    return render(request, 'interfaces_de_inicio/masDesaparecidas.html')

def MasEncontradas(request):
    return render(request, 'interfaces_de_inicio/masEncontradas.html')

def adopcion(request):
    return render(request, 'interfaces_de_inicio/Adopcion.html')

