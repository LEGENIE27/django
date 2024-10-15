from django.db import models

class Medecin(models.Model):
    # Définissez les champs de votre modèle ici
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Patient(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Admin(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class RendezVous(models.Model):
    statut = models.CharField(max_length=50)
    date_rdv = models.DateField()
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)  # Relation avec le médecin
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Relation avec le patient

    def __str__(self):
        return f'Rendez-vous {self.num} - {self.statut}'

class DossierMedical(models.Model):
    historique = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Relation avec le patient

    def __str__(self):
        return f'Dossier {self.num} - Patient {self.patient.nom}'

class Ordonnance(models.Model):
    date_O = models.DateField()
    contenu = models.CharField(max_length=50)
    dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)  # Relation avec le dossier médical

    def __str__(self):
        return f'Ordonnance {self.num} - {self.date_O}'
