from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index_view),
    path("auth/", include("users.urls")),
    path("CRManager/", include("CRManager.urls", namespace="crmanager")),
    path("clients/", include("client.urls", namespace="client")),
]

# python manage.py runserver
# python manage.py startapp ...
# .\venv\Scripts\Activate.ps1
