from django.urls import path
from . import views

app_name = 'crmanager' # Define um namespace para suas URLs do CRM

urlpatterns = [
    path('home/', views.home, name='home'),
    path('leads/', views.leads, name='leads'),
    path('add_leads/', views.add_lead, name='add_lead'),
    path('<int:pk>/', views.leads_detail, name='leads_detail'),
    path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', views.leads_edit, name='leads_edit'),
    path('<int:pk>/convert/', views.convert_to_client, name='convert_to_client')
]