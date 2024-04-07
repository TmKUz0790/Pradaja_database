from django.db import models

# Create your models here.
class Santexnik(models.Model):
    phone = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    target_product = models.CharField(max_length=100)
    standard_installation_count = models.CharField(max_length=100)
    years_of_working = models.CharField(max_length=100)


    def __str__(self):
        return self.phone
