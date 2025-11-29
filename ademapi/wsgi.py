"""WSGI config for the ADEMA Pi project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ademapi.settings")

application = get_wsgi_application()
