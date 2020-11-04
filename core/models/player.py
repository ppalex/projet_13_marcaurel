from django.db import models

class Player(models.Model):

    SEX_CHOICES = (('Masculin', 'M'),('Féminin', 'F'))
    LEVEL_CHOICES = (('D', 'Débutant'), ('I', 'Intermédiaire'), ('A', 'Avancé'))

    player_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)


    def __str__(self):
        return f"{self.firstname} + {self.name}"
