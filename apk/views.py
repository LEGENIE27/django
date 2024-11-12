# apk/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue sur la page d'accueil !")

def home (request):
    return render(request, 'index.html')

def login (request):
    return render(request, 'login.html')

def dashboard (request):
    return render(request, 'dashboard.html')

def doctor_list(request):
    # Code pour récupérer et afficher la liste des médecins
    pass

def patient_list(request):
    # Code pour récupérer et afficher la liste des patients
    pass

def appointment_list(request):
    # Code pour récupérer et afficher la liste des rendez-vous
    pass

def medical_record_list(request):
    # Code pour récupérer et afficher la liste des dossiers médicaux
    pass

def message_list(request):
    # Code pour récupérer et afficher la liste des messages
    pass

def sensitization_list(request):
    # Code pour récupérer et afficher la liste des articles de sensibilisation
    pass

def add_appointment(request):
    # Code pour ajouter un rendez-vous
    pass
