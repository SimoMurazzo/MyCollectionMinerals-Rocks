import os

from django.db import models
from decimal import Decimal
from PIL import Image


def remove_exponent(d):
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()


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
    formula = models.TextField(blank=True)
    environment = models.TextField()
    crystal_system = models.CharField(max_length=120, blank=True)
    cleavage = models.CharField(max_length=120, blank=True)
    hardness = models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True)
    luminescence = models.CharField(max_length=120, blank=True)
    luster = models.CharField(max_length=120, blank=True)
    streak = models.CharField(max_length=120, blank=True)
    pleochroism = models.CharField(max_length=120, blank=True)
    radioactivity = models.CharField(max_length=120, blank=True)
    strunz_class = models.CharField(max_length=10, blank=True)
    image = models.ImageField()

    def save(self, **kwargs):
        super().save(**kwargs)
        height = 320
        im = Image.open(self.image.path)
        new_width = int(im.width / im.height * height)
        thumb = im.resize((new_width, height))
        directory = os.path.dirname(self.image.path)
        filename = os.path.basename(self.image.path)
        thumb.save(f"{directory}/thumb_{filename}")


