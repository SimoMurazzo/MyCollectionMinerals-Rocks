from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    locality = models.TextField(blank=True)
    mass_g = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    size_x_mm = models.PositiveIntegerField(blank=True, null=True)
    size_y_mm = models.PositiveIntegerField(blank=True, null=True)
    size_z_mm = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    rarity = models.CharField(max_length=120)
    formula = models.TextField()
    environment = models.TextField()
    crystal_system = models.CharField(max_length=120)
    cleavage = models.CharField(max_length=120)
    hardness = models.DecimalField(decimal_places=3, max_digits=5)
    luminescence = models.CharField(max_length=120, blank=True)
    luster = models.CharField(max_length=120)
    streak = models.CharField(max_length=120)
    pleochroism = models.CharField(max_length=120, blank=True)
    radioactivity = models.CharField(max_length=120, blank=True)
    strunz_class = models.CharField(max_length=10)
    image = models.ImageField()

