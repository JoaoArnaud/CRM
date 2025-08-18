from django.urls import path

from . import views

app_name = "client"

urlpatterns = [
    path("", views.clients, name="clients"),
    path("<int:pk>/", views.clients_detail, name="clients_detail"),
    path("<int:pk>/delete/", views.client_delete, name="clients_delete"),
    path("<int:pk>/edit/", views.client_edit, name="clients_edit"),
    path("add/", views.add_client, name="add_client"),
]
