"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    # Path del core
    path('', include('core.urls')),
    # Path del inicio
    path('', include('home.urls')),
    # Path del somos
    path('about/', include('about.urls')),
    # Path de convocatoria
    path('announcement/', include('announcement.urls')),
    # Path de Otras publicaciones
    path('other-publish/', include('blogpublish.urls')),
    # Path de formación
    path('formation/', include('formation.urls')),
    # Path de seminarios
    path('seminar/', include('seminar.urls')),
    # Path de contanct
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]

# Añadir
admin.site.site_header = 'Asociación internacional a través del arte'

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)