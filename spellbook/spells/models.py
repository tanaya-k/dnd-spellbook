from django.db import models

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Spell(models.Model):
    name        = models.CharField(max_length = 200)
    classes     = models.ManyToManyField(Classes)
    description = models.CharField(max_length = 5000) # may have to change this to a higher limit
    duration    = models.CharField(max_length = 200)
    level       = models.IntegerField(default=1)
    range       = models.CharField(max_length=100)
    fave        = models.BooleanField(default=False)

    def __str__(self):
        return self.name