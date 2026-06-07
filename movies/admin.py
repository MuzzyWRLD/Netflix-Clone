from django.contrib import admin
from .models import Movie  # Wir holen unseren Bauplan

# Wir legen den Bauplan auf den Schreibtisch des Admins
admin.site.register(Movie)
