"""
URL configuration for netflix_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from movies import views  # NEU: Wir rufen unsere Kellner zur Arbeit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # NEU: Unsere eigene Registrierungs-Seite!
    path('accounts/register/', views.registrieren),

    # NEU: Das leere '' bedeutet: Die absolute Hauptseite (localhost:8000)
    # Wenn jemand dorthin geht, rufe den Kellner "startseite" auf!
    path('', views.startseite),
    path('film/<int:film_id>/', views.film_detail),
]
