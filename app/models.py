from django.contrib.gis.db import models

class POI(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()

    def __str__(self) -> str:
        return self.name