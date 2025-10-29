from django.apps import AppConfig
import os
from django.core.management import execute_from_command_line

class ContactosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactos'


port = os.environ.get("PORT", "8000")  # 8000 de fallback
execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])
