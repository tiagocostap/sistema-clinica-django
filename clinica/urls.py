from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pacientes/', include('pacientes.urls')),
    path('medicos/', include('medicos.urls')),
    path('consultas/', include('consultas.urls')),
]