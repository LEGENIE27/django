# apk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('login.html/', views.login, name='login'),  # Page de connexion
    path('dashboard.html/', views.dashboard, name='dashboard'),
    path('doctors/', views.doctor_list, name='doctor_list'),  # Liste des médecins
    path('patients/', views.patient_list, name='patient_list'),  # Liste des patients
    path('appointments/', views.appointment_list, name='appointment_list'),  # Liste des rendez-vous
    path('medical_records/', views.medical_record_list, name='medical_record_list'),  # Liste des dossiers médicaux
    path('messages/', views.message_list, name='message_list'),  # Liste des messages
    path('sensitizations/', views.sensitization_list, name='sensitization_list'),  # Liste des articles de sensibilisation
    path('appointments/add/', views.add_appointment, name='add_appointment'),  # Ajouter un rendez-vous
    # Ajoute d'autres chemins selon tes besoins
]
