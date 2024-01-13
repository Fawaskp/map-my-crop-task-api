from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

class POI(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "point"]
        unique_together = ["user", "name"]

    def __str__(self):
        return f"{self.name} of {self.user}"