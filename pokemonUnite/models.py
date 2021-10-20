from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100, default='defaultValue')
    desc = models.CharField(max_length=100, default='defaultValue')
    role = models.CharField(max_length=100, default='defaultValue')
    attack_type = models.CharField(max_length=100, default='defaultValue')
    damage_type = models.CharField(max_length=100, default='defaultValue')
    tier = models.CharField(max_length=100, default='defaultValue')
    difficulty = models.CharField(max_length=100, default='defaultValue')
    image = models.CharField(max_length=100, default='defaultValue')
    price_aeos = models.PositiveIntegerField(default=0)
    price_gems = models.PositiveIntegerField(default=0)
