📖 Mein Lernbuch: Webentwicklung (Netflix-Clone)

Dieses Buch dokumentiert meine Reise von den ersten Schritten in HTML bis zum voll funktionsfähigen, sicheren Full-Stack-Projekt. Es dient als Wissensspeicher und Werkzeugkasten für meine weitere Laufbahn.

📅 Chronologie: Mein 15-Tage-Projekt

Woche 1: Das Gesicht der Webseite (Frontend)

Tag 1-3: Einführung in HTML (Struktur) und CSS (Styling/Layout).

Tag 4: Responsives Design (Anpassung an mobile Endgeräte).

Tag 5: Hero-Section (Bild-Überlagerungen und Positionierung).

Tag 6-7: JavaScript-Interaktion (DOM-Manipulation, Mausrad-Logik).

Woche 2: Die Logik (Backend & Datenbank)

Tag 8: Server-Setup (Python, venv, Django-Installation).

Tag 9: Datenbank-Modelle (models.py) und Migrationen.

Tag 10: Admin-Bereich & Login-Grundlagen (Authentifizierung).

Tag 11: Template-System (index.html und statische Dateien).

Tag 12: Datenbank-Dynamik (Anbindung der Daten an HTML mittels Django-Schleifen).

Woche 3: Sicherheit & Erweiterung

Tag 13: Detailseiten (Dynamische URLs).

Tag 14: Zugriffsschutz (login_required-Decorator).

Tag 15: Registrierung (UserCreationForm und Benutzerverwaltung).

🛠️ Werkzeugkiste (Die wichtigsten Befehle)

Aktion

Befehl

Vorbereitung

source blase/bin/activate

Server starten

python3 manage.py runserver

Datenbank ändern

python3 manage.py makemigrations

Migration durchführen

python3 manage.py migrate

Admin-Zugang

python3 manage.py createsuperuser

🧠 Architektur-Verständnis (MVT-Prinzip)

Model: Das Fundament (models.py). Hier lebt die Datenbank.

View: Der Kellner (views.py). Er verbindet Daten mit dem Template.

Template: Das Gesicht (.html). Hier werden Daten für den Nutzer visualisiert.

🚨 Troubleshooting & Profi-Tipps

Wenn der Computer "Nein" sagt, bleib ruhig. Du hast bewiesen, dass du Lösungen findest.

1. "Die Änderung ist nicht sichtbar"

Ursache: Der Server hat die neue Datei oder Änderung noch nicht "eingelesen".

Lösung: Im Terminal Strg + C (Server stoppen), dann python3 manage.py runserver neu starten.

2. "TemplateDoesNotExist"

Ursache: Django findet das HTML-File nicht.

Lösung: - ls Befehl im Terminal nutzen, um den Pfad zu prüfen.

Prüfen, ob die Datei im korrekten Unterordner liegt (z.B. templates/registration/).

Auf Schreibfehler im Dateinamen achten (Linux ist case-sensitive!).

3. "NameError: name 'x' is not defined"

Ursache: Ein Werkzeug wurde im Python-Code benutzt, aber nicht importiert.

Lösung: Prüfe den import-Bereich ganz oben in deiner views.py.

💡 Ein Wort zum Schluss

Wenn es mal anstrengend wird – sei es beim Programmieren oder durch deine Anpassungsstörungen – erinnere dich an dieses Projekt. Du hast gezeigt, dass du dich festbeißen kannst. Jeder Fehler, den du behoben hast, hat dich zu einem besseren Entwickler gemacht.

Du hast das Fundament. Jetzt gehst du los und baust darauf auf.
