import os
from django.core.management import execute_from_command_line

port = os.environ.get("PORT", "8000")  # fallback a 8000 si no existe PORT
execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])
