from django.contrib import admin
from .models import User, Doctor, Patient, DossierMedical, Rendezvous, Ordonnance, Message, Sensibilisation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'is_patient', 'is_doctor')
    search_fields = ('nom', 'email')
    list_filter = ('is_patient', 'is_doctor')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialite', 'adresse_cabinet')
    search_fields = ('user__nom', 'specialite')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'adresse', 'date_naissance')
    search_fields = ('user__nom',)

@admin.register(DossierMedical)
class DossierMedicalAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'historique', 'traitements', 'diagnostics')
    search_fields = ('patient__user__nom', 'medecin__user__nom')

@admin.register(Rendezvous)
class RendezvousAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'date', 'heure', 'statut')
    list_filter = ('statut', 'date')
    search_fields = ('patient__user__nom', 'medecin__user__nom')

@admin.register(Ordonnance)
class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'medicaments', 'duree_traitement')
    search_fields = ('patient__user__nom', 'medecin__user__nom')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'contenu', 'date_envoi')
    search_fields = ('sender__nom', 'receiver__nom')

@admin.register(Sensibilisation)
class SensibilisationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    search_fields = ('titre',)

