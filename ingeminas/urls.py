"""ingeminas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# librerias para estaticos
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from egresados.views import model_form_upload
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('egresados/', include(('egresados.urls', 'egresados'))),
    path('administrador/', include(('administrador.urls','administrador'))),
    path('empresas/', include(('empresas.urls', 'empresas'))),
    path('empleo/', include(('empleo.urls', 'empleos'))),
    path('convocatorias/', include(('convocatorias.urls', 'convocatorias'))),
url(r'^uploads/form/$', model_form_upload, name='model_form_upload'),    path('', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
