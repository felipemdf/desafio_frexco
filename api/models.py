from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=30, blank=False)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, blank= False)

    def __str__(self) -> str:
        return self.name