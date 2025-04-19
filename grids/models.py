from django.db import models

# Create your models here.

class Grid(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"Grid ({self.x}, {self.y}, {self.width}, {self.height})"

