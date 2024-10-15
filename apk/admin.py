from django.contrib import admin
from .models import Medecin, Patient, Admin, RendezVous, DossierMedical, Ordonnance

# Enregistrement des modèles avec l'interface d'administration
@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'specialite')  # Champs à afficher dans la liste

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('statut', 'date_rdv', 'medecin', 'patient')

@admin.register(DossierMedical)
class DossierMedicalAdmin(admin.ModelAdmin):
    list_display = ('historique', 'patient')

@admin.register(Ordonnance)
class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('date_O', 'contenu', 'dossier_medical')
