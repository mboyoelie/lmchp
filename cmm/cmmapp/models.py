from django.db import models

# Create your models here.
class patient (models.Model):
    numeroFiche = models.BigIntegerField(default=0)
    dateNaissaince = models.DateField()
    noms = models.CharField(max_length=200, blank=True)
    age = models.IntegerField()
    sexe = models.CharField(max_length=12)
    telephone = models.BigIntegerField()
    adresse = models.TextField(blank=True)
    email = models.CharField(max_length=25)
    dateArrive = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.noms

class utilisateur (models.Model):
    noms = models.CharField(max_length=200)
    sexe = models.CharField(max_length=12)
    telephone = models.BigIntegerField()
    adresse = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.noms


class categorie (models.Model):
    categories = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.categories

class allergie (models.Model):
    allergies = models.TextField(blank=True)
    def __str__(self):
        return self.allergies

class contreIndication (models.Model):
    contreIndications = models.TextField(blank=True)
    def __str__(self):
        return self.contreIndications

class triage (models.Model):
    poidsA = models.CharField(max_length=50,blank=True)
    poidsN = models.CharField(max_length=50,blank=True)
    taille = models.CharField(max_length=10,blank=True)
    temperature = models.CharField(max_length=10,default=0)
    pressionArterielle = models.CharField(max_length=15)
    battementCardiaque= models.CharField(max_length=15,blank=True)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.poidsA


class rdv (models.Model):
    date = models.DateField()
    heure = models.TimeField()
    observation = models.TextField()

    def __str__(self):
        return self.observation
