from django.db import models

# Create your models here.


class Campus(models.Model):
    codecampus = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    
    def __str__(self):
        return self.campus
