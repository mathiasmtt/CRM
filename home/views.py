from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from .forms import CustomUserCreationForm

def home(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/index.html', {'user_groups': user_groups})

def about_us(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/about_us.html', {'user_groups': user_groups})

def contact_us(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/contact_us.html', {'user_groups': user_groups})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar el usuario al grupo "Clientes" por defecto
            clientes_group = Group.objects.get(name='Clientes')
            user.groups.add(clientes_group)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/profile.html', {'user_groups': user_groups})
