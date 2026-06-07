from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # NEU: Der Türsteher
from django.contrib.auth import login  # NEU: Loggt Nutzer per Code ein
from django.contrib.auth.forms import UserCreationForm  # NEU: Djangos fertiges Formular
from .models import Movie

# NEU: Der Stempel blockiert diese Funktion für unangemeldete Gäste
@login_required
def startseite(request):
    alle_filme = Movie.objects.all()
    return render(request, 'index.html', {'filme': alle_filme})

# NEU: Auch die Detailseite wird abgesperrt
@login_required
def film_detail(request, film_id):
    einzelner_film = Movie.objects.get(id=film_id)
    return render(request, 'detail.html', {'film': einzelner_film})

# --- NEU: TAG 15 - Die Registrierung ---
def registrieren(request):
    # Wenn der Nutzer auf "Registrieren" geklickt hat (Daten abschicken)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()         # 1. Speichert den neuen Nutzer in der Datenbank
            login(request, user)       # 2. Loggt ihn sofort automatisch ein
            return redirect('/')       # 3. Schickt ihn direkt zur Startseite

    # Wenn der Nutzer die Seite nur normal aufruft (leeres Formular zeigen)
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
