"""Core application views for ADEMA Pi."""
from __future__ import annotations

import platform
import socket

import django
from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def _database_engine_label() -> str:
    engine = connection.settings_dict.get("ENGINE", "")
    if "postgresql" in engine:
        return "PostgreSQL"
    return "SQLite"


def home(request: HttpRequest) -> HttpResponse:
    context = {
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "django_version": django.get_version(),
        "database_engine": _database_engine_label(),
    }
    return render(request, "core/home.html", context)


def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok", "app": "ademapi"})
