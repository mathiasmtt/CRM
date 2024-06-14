from django.shortcuts import render

def index(request):
    return render(request, 'modulo_propietarios/index.html')
