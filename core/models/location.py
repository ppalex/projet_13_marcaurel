from django.contrib.gis.db import models


class Location(models.Model):
    coordinates = models.PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.coordinates, 'coords', [])[::-1])
