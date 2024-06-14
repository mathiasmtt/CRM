from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required

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
            try:
                guest_group = Group.objects.get(name='Guest')
                user.groups.add(guest_group)
            except Group.DoesNotExist:
                # Manejar el error si el grupo no existe
                print("El grupo 'Guest' no existe.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/profile.html', {'user_groups': user_groups})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/edit_profile.html', {'form': form, 'user_groups': user_groups})

def contabilidad(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/contabilidad.html', {'user_groups': user_groups})

def financiero(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/financiero.html', {'user_groups': user_groups})

def societario(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'home/societario.html', {'user_groups': user_groups})
