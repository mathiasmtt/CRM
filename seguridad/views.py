from django.shortcuts import render
from django.contrib.auth.models import User  # Añadir esta línea para importar User

def index(request):
    return render(request, 'seguridad/index.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'seguridad/user_list.html', {'users': users})
