from django.db import models

class Position(models.Model):
    POSITION_CHOICES =  (("keeper", "Gardien"), 
                                ("defensive", "Défenseur"),
                                ("forward", "Attaquant"),
                                ("center", "Milieu"))

    position_name = models.CharField(max_length=255, choices=POSITION_CHOICES)