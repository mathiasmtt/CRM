from django.shortcuts import render

def index(request):
    return render(request, 'modulo_clientes/index.html')
