from django.contrib.gis.db import models


class Location(models.Model):
    coordinates = models.PointField()

    @property
    def lat_lng(self):
        """This method returns a list of coordinates.

        Returns:
            List: Contains the coordinates: [lat, lng].
        """
        return list(getattr(self.coordinates, 'coords', [])[::-1])
