"""
URL configuration for clubdelqr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# clubdelqr/urls.py
from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('about_us/', home_views.about_us, name='about_us'),
    path('contact_us/', home_views.contact_us, name='contact_us'),
    path('register/', home_views.register, name='register'),
    path('profile/', home_views.profile, name='profile'),  # Mantener esta línea
    path('edit_profile/', home_views.edit_profile, name='edit_profile'),  # Añadir esta línea
    path('contabilidad/', home_views.contabilidad, name='contabilidad'),  # Añadir esta línea
    path('financiero/', home_views.financiero, name='financiero'),  # Añadir esta línea
    path('societario/', home_views.societario, name='societario'),  # Añadir esta línea
    path('accounts/', include('django.contrib.auth.urls')),  # Asegúrate de que esta línea está presente
    path('propietarios/', include('modulo_propietarios.urls')),
    path('clientes/', include('modulo_clientes.urls')),
    path('seguridad/', include('seguridad.urls')),
]
