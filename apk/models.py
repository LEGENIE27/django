from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom']

    def __str__(self):
        return self.nom

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)
    adresse_cabinet = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.user.nom} - {self.specialite}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    date_naissance = models.DateField()

    def __str__(self):
        return self.user.nom

class DossierMedical(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    historique = models.TextField()
    traitements = models.TextField()
    diagnostics = models.TextField()

    def __str__(self):
        return f"Dossier de {self.patient.user.nom} - Dr. {self.medecin.user.nom}"

class Rendezvous(models.Model):
    STATUT_CHOICES = [
        ('en attente', 'En attente'),
        ('confirmé', 'Confirmé'),
        ('annulé', 'Annulé'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    description = models.TextField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='en attente')

    def __str__(self):
        return f"Rendez-vous de {self.patient.user.nom} avec Dr. {self.medecin.user.nom}"

class Ordonnance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicaments = models.TextField()
    duree_traitement = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"Ordonnance pour {self.patient.user.nom} - Dr. {self.medecin.user.nom}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.sender.nom} à {self.receiver.nom}"

class Sensibilisation(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre
