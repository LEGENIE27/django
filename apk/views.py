# apk/views.py
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages

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

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        mot_de_passe = request.POST['mot_de_passe']

        # Authentification de l'utilisateur
        user = authenticate(request, username=email, password=mot_de_passe)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirection vers le tableau de bord
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    
    return render(request, 'login.html')